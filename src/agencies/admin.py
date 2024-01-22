from django.contrib import admin

# Register your models here.
from .models import Agency


class AgencyAdmin(admin.ModelAdmin):
    list_display = ["agency_name", "agency_description", "agency_url"]
    search_fields = ["agency_name", "agency_description", "agency_url"]

    class Meta:
        model = Agency


admin.site.register(Agency, AgencyAdmin)
