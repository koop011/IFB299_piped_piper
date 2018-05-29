import datetime
from datetime import date
from django.utils.translation import gettext_lazy as _
from .models import StudentData
from django.contrib import admin


class AgeFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Age Bracket')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'AgeBracket'


    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('Over 18', _('Adult')),
            ('Under 18', _('Child')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value
        # to decide how to filter the queryset.
        today = datetime.date.today()

        if self.value() == 'Over 18':
            return queryset.filter(DoB__gte=date(1800, 1, 1),
                                   DoB__lte=datetime.date.today() - datetime.timedelta(weeks=938))
        if self.value() == 'Under 18':
            return queryset.filter(DoB__gte=datetime.date.today() - datetime.timedelta(weeks=938),
                                   DoB__lte=datetime.date.today())

class StudentAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'UserName', 'DoB', 'Gender', 'Email' , 'pNumber', 'year_born_in')
    list_filter = ('Gender', AgeFilter)

    search_fields = ('FirstName', 'LastName', 'UserName', 'Email')


admin.site.site_header = 'Pinelands Music School Administration Page'
admin.site.register(StudentData, StudentAdmin)
