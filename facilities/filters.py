from django.db.models import Q
from .models import Facility

def filter_facilities(qs, params):
    q = params.get("q")
    ftype = params.get("type")
    partner = params.get("partner")
    location = params.get("location")
    capability = params.get("capability")

    if q:
        qs = qs.filter(
            Q(name__icontains=q) |
            Q(description__icontains=q) |
            Q(capabilities__icontains=q) |
            Q(location__icontains=q) |
            Q(partner_organization__icontains=q)
        )

    if ftype:
        qs = qs.filter(facility_type__iexact=ftype)

    if partner:
        qs = qs.filter(partner_organization__icontains=partner)

    if location:
        qs = qs.filter(location__icontains=location)

    if capability:
        # match capability token anywhere in the capabilities list
        qs = qs.filter(capabilities__icontains=capability)

    return qs
