from django.contrib import admin
from .models import TeacherData

# Register your models here.

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'DoB', 'email', 'pNumber', 'certificates')
    list_filter = ('certificates', 'electric_guitar', 'guitar', 'keyboard', 'piano', 'drums', 'violin', 'saxophone', 'flute', 'cello', 'clarinet')
    search_fields = ('fname', 'lname', 'email')


admin.site.register(TeacherData, TeachersAdmin)