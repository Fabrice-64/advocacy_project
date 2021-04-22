from django.contrib import admin
import communities.models as comms
# Register your models here.

@admin.register(comms.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(comms.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dept_number']

@admin.register(comms.City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(comms.Intercom)
class IntercomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department']