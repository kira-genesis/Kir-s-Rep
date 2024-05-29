from django.http import HttpResponse
from django.template import loader 
from django.shortcuts import render
from . import models 
import statistics

def __unpack(value, field):
    result = []
    for item in value:
        result.append(getattr(item, field))
    return result

def index(request):
    template = loader.get_template("kirsApp/index.html")

    rating = {}

    for subject in models.Subject.objects.all():
        subject_name = subject.__str__()
        rating[subject_name] = {}
        for student in models.Student.objects.all():
            student_name = student.__str__()
            marks = __unpack(models.Marks.objects.filter(student=student, subject=subject), 'score')
            median_mark = statistics.median(marks) if len(marks) > 0 else 0
            rating[subject_name][student_name] = median_mark
        rating[subject_name] = dict(sorted(rating[subject_name].items(), key=lambda item: item[1], reverse=True))

    context = {
        'list_object': rating
    }

    return HttpResponse(
        template.render(context, request)
    )