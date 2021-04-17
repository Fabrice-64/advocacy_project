from django.contrib import admin
import officials.models as off
# Register your models here.

@admin.register(off.Official)
class OfficialAdmin(admin.ModelAdmin):
    pass


@admin.register(off.NationalMandate)
class NationalMandateAdmin(admin.ModelAdmin):
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