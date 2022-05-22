from django.shortcuts import render

from tables.models import Student, Teacher


def show_student_table(request):  # Displays students table
    student_list = Student.objects.all()
    return render(request, 'show_student_table.html',
                  {'student_list': student_list})


def show_teacher_table(request):  # Displays teachers table
    teacher_list = Teacher.objects.all()
    return render(request, 'show_teacher_table.html',
                  {'teacher_list': teacher_list})
