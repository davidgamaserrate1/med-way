from django.contrib import admin
from django.urls import path
from medway_api.views.exams import (
    send_exam,
    get_exam_results,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("exam/send", send_exam),
    path('exam/<int:exam_id>/student/<int:student_id>/results', get_exam_results)
]
