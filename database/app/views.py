from django.shortcuts import render
from .models import Student, Course

def index(request):
    # students = Student.object.filter(course__name='History')
    # courses = Student.object.get(ig=2).course.all()
    python = Course.object.get(name='Python')
    student, _ = python.student_set.get_or_create(name="Bob")
    student = Student.object.creste(name='Tom')
    res = python.student_set.add(student)
    return render(request, '', context={'students': student})

