from django.shortcuts import render

from .forms import (
    StudentForm,
    StudentNameForm,
    StudentGradeForm,
)
from .models import StudentModel

from django.http import HttpResponse
from .student import Student

def filter_group_by_students(request):

    form = StudentNameForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            student_name = form.cleaned_data['student_name']
            group = Student.objects.filter(student=student_name)

            context = {
                'students': students,
            }

            return render(
                request,
                template_name='students.html',
                context=context
           )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='group_form.html',
        context=context
    )



def get_all_students(request):

    students = StudentModel.objects.all()

    context = {
        'students': students,
    }

    return render(
        request,
        template_name='students.html',
        context=context
   )


def get_student(request, visit_id):

    group = Student.objects.get(id=group_id)

    context = {
        'student': student,

    }

    return render(
        request,
        template_name='group.html',
        context=context,
    )


def add_student(request):

    form = StudentForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():


            student = Student(
                name=form.cleaned_data['student'],
                grade=form.cleaned_data['grade'],
                average_grade=form.cleaned_data['average_grade'],
            )

            student.save()

            context = {
                "student":student,
            }

            return render(
                request,
                template_name='group.html',
                context=context,
            )

    return render(
        request,
        template_name='student_form.html',
        context={'form': form}
    )


