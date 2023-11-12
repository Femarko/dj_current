from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


# def students_list(request):
#     SORT_MAP = {
#         'name': 'name',
#         'group': 'group',
#         'teacher': 'teacher'
#     }
#
#     template = 'school/students_list.html'
#     object_list = Student.objects.order_by('group')
#     ordering = request.GET.get('group')
#     if ordering:
#         object_list = object_list.order_by(SORT_MAP[ordering])
#     context = {
#         'object_list': object_list,
#     }
#     print(object_list)
#     for student in object_list:
#         teachers = student.teachers.all()
#         print(teachers)
#
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     # ordering = 'group'
#
#     return render(request, template, context)

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