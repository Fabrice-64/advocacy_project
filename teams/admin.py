from django.contrib import admin
from teams.models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "city"]


admin.site.register(Team, TeamAdmin)
