from django.contrib import admin
from .models import Question, Choice, Submission
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin


class QuestionInline(admin.TabularInline):
    model = Choice
    extra = 3


class ChoiceInline(admin.TabularInline):
    model = Submission
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    search_fields = ['question_text']
    inlines = [QuestionInline, ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id',)
