from django.contrib import admin
from .models import electric_guitar_half_hour, electric_guitar_hour, keyboard_half_hour, keyboard_hour, piano_half_hour, piano_hour, guitar_half_hour, guitar_hour, drums_half_hour, drums_hour, violin_half_hour, violin_hour, saxophone_half_hour, saxophone_hour, flute_half_hour, flute_hour, cello_half_hour, cello_hour, clarinet_half_hour, clarinet_hour,pendingLessonContracts_new, pendingLessonContracts_old

# Register your models here.
admin.site.register(electric_guitar_half_hour)
admin.site.register(electric_guitar_hour)
admin.site.register(keyboard_half_hour)
admin.site.register(keyboard_hour)
admin.site.register(piano_half_hour)
admin.site.register(piano_hour)
admin.site.register(guitar_half_hour)
admin.site.register(guitar_hour)
admin.site.register(drums_half_hour)
admin.site.register(drums_hour)
admin.site.register(violin_half_hour)
admin.site.register(violin_hour)
admin.site.register(saxophone_half_hour)
admin.site.register(saxophone_hour)
admin.site.register(flute_half_hour)
admin.site.register(flute_hour)
admin.site.register(cello_half_hour)
admin.site.register(cello_hour)
admin.site.register(clarinet_half_hour)
admin.site.register(clarinet_hour)

class ContractAdminNew(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'instrument', 'contract_period')



class ContractAdminOld(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'instrument', 'contract_period')

admin.site.register(pendingLessonContracts_new, ContractAdminNew)
admin.site.register(pendingLessonContracts_old, ContractAdminOld)