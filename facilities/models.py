from django.db import models

class Facility(models.Model):
    class FacilityType(models.TextChoices):
        LAB = "Lab", "Lab"
        WORKSHOP = "Workshop", "Workshop"
        TESTING_CENTER = "Testing Center", "Testing Center"
        OTHER = "Other", "Other"

    name = models.CharField(max_length=150, unique=True)
    location = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    partner_organization = models.CharField(max_length=150, blank=True)
    facility_type = models.CharField(max_length=32, choices=FacilityType.choices, default=FacilityType.LAB)
    capabilities = models.TextField(help_text="Comma-separated capabilities, e.g. CNC, PCB fabrication, materials testing")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["facility_type"]),
            models.Index(fields=["partner_organization"]),
            models.Index(fields=["location"]),
        ]

    def __str__(self):
        return self.name

    def capabilities_list(self):
        # Return a normalized list of capabilities
        return [c.strip() for c in self.capabilities.split(",") if c.strip()]
