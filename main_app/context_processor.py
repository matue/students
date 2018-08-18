from django.template.context import *
from main_app.models import Student

def Students(request):
    return {"student_list": Student.objects.all()}