from django.contrib import admin
from .models import Facility

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "facility_type", "partner_organization", "location", "created_at")
    search_fields = ("name", "partner_organization", "location", "capabilities", "description")
    list_filter = ("facility_type", "partner_organization", "location", "created_at")
