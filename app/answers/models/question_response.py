from django.db import models
from question.models.question import Question
from answers.models.exam_response import ExamResponse

class QuestionResponse(models.Model):
    exam_response = models.ForeignKey(ExamResponse, on_delete=models.CASCADE, related_name="question_responses")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1)  
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.id} - {'Correta' if self.is_correct else 'Errada'}"
