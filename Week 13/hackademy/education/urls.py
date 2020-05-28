from django.urls import path, include

from education.views import index, courses, lectures

app_name = 'education'

courses_patterns = [
    path('', courses.list, name='list'),
    path('<int:course_id>/', courses.detail, name='detail'),
    path('<int:pk>/edit/', courses.CourseUpdateView.as_view(), name='edit'),
    path('new/', courses.CourseCreateView.as_view(), name='create'),
]

lectures_patterns = [
    path('', lectures.list, name='list'),
    path('<uuid:lecture_id>/', lectures.detail, name='detail'),
]

urlpatterns = [
    path('', index, name='index'),
    path('courses/', include((courses_patterns, 'courses'))),
    path('lectures/', include((lectures_patterns, 'lectures'))),
]
