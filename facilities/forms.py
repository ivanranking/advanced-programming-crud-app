from django import forms
from .models import Facility

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ["name", "location", "description", "partner_organization", "facility_type", "capabilities"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "capabilities": forms.Textarea(attrs={"rows": 3, "placeholder": "e.g. CNC, PCB fabrication, materials testing"}),
        }

    def clean_capabilities(self):
        caps = self.cleaned_data.get("capabilities", "")
        # Normalize: remove duplicate entries, keep order
        seen = set()
        normalized = []
        for raw in caps.split(","):
            item = raw.strip()
            if not item:
                continue
            key = item.lower()
            if key not in seen:
                seen.add(key)
                normalized.append(item)
        return ", ".join(normalized)
