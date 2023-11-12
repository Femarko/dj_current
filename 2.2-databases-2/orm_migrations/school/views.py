from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher

def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.all()
    context = {
        'object_list': object_list,
    }
    print(f'object_list: {object_list}')
    profs = Teacher.objects.all()
    print(f'profs: {profs}')
    for student in object_list:
        print(f'student: {student}')
        print(f'student.teachers.all(): {student.teachers.all()}')
    return render(request, template, context)