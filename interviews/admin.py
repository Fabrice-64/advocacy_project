from django.contrib import admin
import interviews.models as itw
# Register your models here.

@admin.register(itw.AdvocacyTopic)
class AdvocacyTopicAdmin(admin.ModelAdmin):
    fields = ('created_by', 'source', 'key_statement', 'quote')


@admin.register(itw.Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass

