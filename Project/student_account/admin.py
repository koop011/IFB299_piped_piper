import datetime

from django.contrib import admin
from .models import StudentData
from django.contrib.admin.filters import DateFieldListFilter


class MyDateTimeFilter(DateFieldListFilter):
    def __init__(self, *args, **kwargs):
        super(MyDateTimeFilter, self).__init__(*args, **kwargs)
        
        today = datetime.now()

        self.links += ((
            (_('Under 18'), {
                self.lookup_kwarg_since: str(today),
                self.lookup_kwarg_until: str(today - datetime.timedelta(years=18)),
            }),
        ))

# min_age = 24
# max_date = date.today()
# try:
#     max_date = max_date.replace(year=max_date.year - min_age)
# except ValueError: # 29th of february and not a leap year
#     assert max_date.month == 2 and max_date.day == 29
#     max_date = max_date.replace(year=max_date.year - min_age, month=2, day=28)
# StudentData = StudentData.objects.filter(DoB=max_date)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'UserName', 'DoB', 'Gender', 'Email' , 'pNumber')
    list_filter = ('Gender', 'DoB')
    search_fields = ('FirstName', 'LastName', 'UserName', 'Email')


admin.site.site_header = 'Pinelands Music School Administration Page'
admin.site.register(StudentData, StudentAdmin)
