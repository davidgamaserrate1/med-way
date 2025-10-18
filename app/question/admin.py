from django.contrib import admin

from question.models.question import Question
from question.models.alternative import Alternative


class AlternativeInline(admin.TabularInline):
    model = Alternative
    min_num = 1
    max_num = 5
    ordering = ('option',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AlternativeInline]
