from django.contrib import admin
from . models import Missions, PersonalizedAdvice, ForumInformation

admin.site.register(Missions)
admin.site.register(PersonalizedAdvice)
admin.site.register(ForumInformation)