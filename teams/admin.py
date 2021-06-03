from django.contrib import admin
from teams.models import Team
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "city"]

admin.site.register(Team, TeamAdmin)
