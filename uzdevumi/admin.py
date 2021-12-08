from django.contrib import admin
from .models import StudentModel


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(StudentModel, StudentAdmin)