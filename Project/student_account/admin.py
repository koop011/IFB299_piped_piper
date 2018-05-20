from django.contrib import admin
from .models import StudentData

class StudentAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'UserName', 'DoB', 'Gender', 'Email' , 'pNumber')
    list_filter = ('Gender', 'DoB')
    search_fields = ('FirstName', 'LastName', 'UserName')


admin.site.site_header = 'Administration'
admin.site.register(StudentData, StudentAdmin)
