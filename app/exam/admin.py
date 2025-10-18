from django.contrib import admin

from exam.models.exam import Exam
from exam.models.exam_question import ExamQuestion

class ExamQuestionInline(admin.TabularInline):
    model = ExamQuestion


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    inlines = [ExamQuestionInline]
