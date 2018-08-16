from django.contrib import admin
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]


admin.site.register(Student, StudentAdmin)
admin.site.register(Group)