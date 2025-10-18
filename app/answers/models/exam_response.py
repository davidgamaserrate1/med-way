from django.db import models
from student.models import Student
from exam.models.exam import Exam


class ExamResponse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="exam_responses")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="responses")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.exam.name}"