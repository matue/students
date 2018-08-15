from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=30)

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Student(models.Model):
    first_name = models.CharField(max_length=30, blank=False, default='')
    last_name = models.CharField(max_length=30, blank=False, default='')
    middle_name = models.CharField(max_length=30, blank=False, default='')
    birth_day = models.DateField(blank=True, default='')
    stud_number = models.CharField(max_length=10)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default='')
    is_captain = models.BooleanField(blank=False)

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'







