from django.contrib import admin
import officials.models as off


@admin.register(off.Official)
class OfficialAdmin(admin.ModelAdmin):
    model = off.Official
    list_display = ['first_name', 'last_name']


@admin.register(off.MPMandate)
class MPMandateAdmin(admin.ModelAdmin):
    pass


@admin.register(off.SenatorMandate)
class SenatorMandateAdmin(admin.ModelAdmin):
    pass


@admin.register(off.MandateCity)
class MandateCityAdmin(admin.ModelAdmin):
    pass


@admin.register(off.MandateDepartment)
class MandateDepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(off.MandateInterCom)
class MandateIntercomAdmin(admin.ModelAdmin):
    pass


@admin.register(off.MandateRegion)
class MandateRegionAdmin(admin.ModelAdmin):
    pass
