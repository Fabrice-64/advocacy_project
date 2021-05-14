from django.contrib import admin
import interviews.models as itw
# Register your models here.

@admin.register(itw.AdvocacyTopic)
class AdvocacyTopicAdmin(admin.ModelAdmin):
    fields = ('is_active', 'keyword', 'created_by', 'source_title', 'source', 'key_statement', 'slug', 'quote')
    prepopulated_fields = {'slug': ('key_statement',)}


@admin.register(itw.Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass

