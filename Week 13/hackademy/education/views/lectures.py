from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from education.models import Course, Lecture


def list(request):
    return render(request, 'lectures/list.html',
                  {'lectures': Lecture.objects.order_by('course')})


def detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    return render(request, 'lectures/detail.html',
                  {'lecture': lecture})
