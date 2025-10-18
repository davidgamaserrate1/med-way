from django.contrib import admin
from answers.models.exam_response import ExamResponse
from answers.models.question_response import QuestionResponse


class QuestionResponseInline(admin.TabularInline):
    model = QuestionResponse
    extra = 0
    readonly_fields = ("question", "selected_option", "is_correct")
    can_delete = False  # evita deletar respostas diretamente pelo inline


@admin.register(ExamResponse)
class ExamResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "exam", "nota_percentual", "total_questoes", "created_at")
    list_filter = ("exam", "student")
    search_fields = ("student__name", "exam__name")
    inlines = [QuestionResponseInline]  # mostra as respostas da prova inline

    def total_questoes(self, obj):
        return obj.question_responses.count()
    total_questoes.short_description = "Total de Questões"

    def nota_percentual(self, obj):
        total = obj.question_responses.count()
        if total == 0:
            return 0
        acertos = obj.question_responses.filter(is_correct=True).count()
        return round((acertos / total) * 100, 2)
    nota_percentual.short_description = "Nota (%)"


@admin.register(QuestionResponse)
class QuestionResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "exam_response", "question", "selected_option", "is_correct")
    list_filter = ("is_correct", "exam_response__exam")
    search_fields = ("question__content", "exam_response__student__name")
