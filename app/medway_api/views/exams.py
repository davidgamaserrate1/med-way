import json
from exam.models.exam import Exam
from answers.models.exam_response import ExamResponse
from answers.models.question_response import QuestionResponse
from question.models.question import Question
from student.models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["POST"])
def send_exam(request):
    try:
        data = json.loads(request.body)
        exam_id = data.get("exam")
        student_id = data.get("student")  
        questions_data = data.get("questions")

        if not all([exam_id, student_id, questions_data]):
            return Response(
                {"mensagem": "Campos 'exam', 'student' e 'questions' são obrigatórios."},
                status=400
            )

        exam = Exam.objects.filter(pk=exam_id).first()
        if not exam:
           return Response( {"mensagem": "Exame não encontrado."}, status=404 ) 
        
        student = Student.objects.filter(pk=student_id).first()
        if not student:
           return Response( {"mensagem": "Estudante não encontrado."}, status=404 )
        
        exam_questions = exam.questions.all()
        exam_question_ids = {q.id for q in exam_questions}

        resultados = []
        acertos = 0

        exam_response = ExamResponse.objects.create(student=student, exam=exam)

        for item in questions_data:
            question_id = item.get("question")
            resposta_usuario = item.get("response")

            if question_id not in exam_question_ids:
                resultados.append({
                    "question_id": question_id,
                    "mensagem": "Questão não pertence a este exame.",
                    "acertou": False
                })
                continue

            question = Question.objects.get(pk=question_id)
            alternativa_correta = question.alternatives.filter(is_correct=True).first()

            acertou = (
                alternativa_correta and
                resposta_usuario.strip().upper() == chr(64 + alternativa_correta.option)
            )

            QuestionResponse.objects.create(
                exam_response=exam_response,
                question=question,
                selected_option=resposta_usuario.strip().upper(),
                is_correct=acertou
            )

            if acertou:
                acertos += 1

            resultados.append({
                "question_id": question_id,
                "question": question.content,
                "resposta_usuario": resposta_usuario,
                "correta": chr(64 + alternativa_correta.option) if alternativa_correta else None,
                "acertou": acertou
            })

        return Response({
            "prova": exam.name,
            "estudante": student.name,
            "mensagem": "Respostas salvas e processadas com sucesso.",
            "total_questoes": len(resultados),
            "total_acertos": acertos,
            "nota_percentual": round((acertos / len(resultados)) * 100, 2) if resultados else 0,
            "resultado": resultados,
            "success": True
        }, status=201)

    except json.JSONDecodeError:
        return Response({"mensagem": "JSON inválido."}, status=400)
    except Exception as e:
        return Response({"mensagem": f"Erro interno: {str(e)}"}, status=500)
    

@api_view(["GET"])
def get_exam_results(request, exam_id, student_id):
    exam_response = (
        ExamResponse.objects
        .filter(exam_id=exam_id, student_id=student_id)
        .order_by('-created_at')
        .first()
    )

    if not exam_response:
        return Response({"mensagem": "Respostas não encontradas."}, status=404)

    respostas = exam_response.question_responses.all()
    total = respostas.count()
    acertos = respostas.filter(is_correct=True).count()

    resultado = [
        {
            "question": r.question.content,
            "resposta_usuario": r.selected_option,
            "acertou": r.is_correct
        } for r in respostas
    ]

    return Response({
        "prova": exam_response.exam.name,
        "estudante": exam_response.student.name,
        "total_questoes": total,
        "total_acertos": acertos,
        "nota_percentual": round((acertos / total) * 100, 2) if total else 0,
        "respostas": resultado
    })
