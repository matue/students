from django.contrib import admin
from .models import *


class StudentsInLine(admin.TabularInline):
    model = Student
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]


class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentsInLine]


admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)