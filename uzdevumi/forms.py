from django.forms import (
    Form,
    CharField,
    FloatField,
)


class StudentForm(Form):

    student = CharField()
    grades = CharField()


class StudentNameForm(Form):

    student_name = CharField()


class StudentGradeForm(Form):

    average_grade = FloatField()