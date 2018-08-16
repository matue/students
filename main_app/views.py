from django.shortcuts import render
from .models import *


def GroupList(request):
    queryset = Student.objects.filter(is_captain=True).order_by('group__group_name')
    return render(request, 'group_list.html', {'object_list': queryset})


def StudentList(request, group):
    queryset = Student.objects.filter(group=group)
    return render(request, 'student_list.html', {'object_list': queryset,
                                                 'group': group})


