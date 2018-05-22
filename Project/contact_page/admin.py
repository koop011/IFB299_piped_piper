from django.contrib import admin
from .models import TeacherData
# Register your models here.

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'DoB', 'email', 'pNumber')
    list_filter = ('certificates', 'subjects')
    search_fields = ('fname', 'lname', 'email')


admin.site.register(TeacherData, TeachersAdmin)