from django.contrib import admin
from app.models import Question, Answer, UserProfile

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserProfile)
