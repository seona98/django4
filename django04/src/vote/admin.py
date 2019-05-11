from django.contrib import admin
from vote.models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)
