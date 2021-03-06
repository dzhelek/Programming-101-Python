from django.contrib import admin

# Register your models here.
from education.models import Course, Lecture, Task, Solution


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'get_duration',
                    'start_date', 'end_date')

    def get_duration(self, obj):
        if obj.duration:
            return f'{obj.months_duration} months'

        return 'N/A'

    get_duration.short_description = 'Duration'


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'week', 'course', 'url')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'due_date',
                    'course', 'lecture')


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('task', 'date', 'url')
