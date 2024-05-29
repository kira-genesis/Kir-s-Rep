from django.db import models

class Student(models.Model):
    fisrt_name = models.TextField(max_length=255)
    last_name  = models.TextField(max_length=255)
    course     = models.IntegerField()

    def __str__(self):
        return "{first} {last}".format(first=self.fisrt_name, last=self.last_name).strip()

class Subject(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Marks(models.Model):
    score   = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        subject = self.subject.__str__()
        student_name = self.student.__str__()

        return "{student} got {score} on ({subject})".format(student=student_name, score=self.score, subject=subject)