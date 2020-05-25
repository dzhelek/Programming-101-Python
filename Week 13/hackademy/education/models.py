import uuid

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True)

    def __str__(self):
        return f'Course "{self.name}"'

    @property
    def duration(self):
        if self.end_date:
            return self.end_date - self.start_date


class Lecture(models.Model):
    # identifier = models.IntegerField(unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=250)
    week = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f'Lecture "{self.name}"'


class Task(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    due_date = models.DateField(default=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.DO_NOTHING,
                                blank=True, null=True)

    def __str__(self):
        return f'Task "{self.name}"'


class Solution(models.Model):
    def github_validator(url):
        if 'github.com' not in url:
            raise ValidationError('not a github link')

    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    date = models.DateField(default=timezone.now)
    url = models.URLField(validators=[URLValidator, github_validator])

    def __str__(self):
        return f'Solution "{self.task}"'
