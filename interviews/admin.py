from django.contrib import admin
import interviews.models as itw
# Register your models here.

@admin.register(itw.AdvocacyTopic)
class AdvocacyTopicAdmin(admin.ModelAdmin):
    pass


@admin.register(itw.Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass


