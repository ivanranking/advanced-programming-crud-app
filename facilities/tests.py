from django.test import TestCase
from django.urls import reverse
from .models import Facility

class FacilityTests(TestCase):
    def setUp(self):
        Facility.objects.create(
            name="UIRI Maker Lab",
            location="Kampala",
            description="Test lab",
            partner_organization="UIRI",
            facility_type=Facility.FacilityType.LAB,
            capabilities="CNC, PCB fabrication, Materials testing",
        )
        Facility.objects.create(
            name="CEDAT Workshop",
            location="Kampala",
            description="Workshop for prototyping",
            partner_organization="Makerere",
            facility_type=Facility.FacilityType.WORKSHOP,
            capabilities="Welding, 3D printing",
        )

    def test_list_view(self):
        url = reverse("facilities:list")
        resp = self.client.get(url)
        self.assertContains(resp, "UIRI Maker Lab")
        self.assertContains(resp, "CEDAT Workshop")

    def test_search_filter(self):
        url = reverse("facilities:list")
        resp = self.client.get(url, {"q": "UIRI"})
        self.assertContains(resp, "UIRI Maker Lab")
        self.assertNotContains(resp, "CEDAT Workshop")

        resp = self.client.get(url, {"type": "Workshop"})
        self.assertContains(resp, "CEDAT Workshop")
        self.assertNotContains(resp, "UIRI Maker Lab")

    def test_create_edit_delete(self):
        create_url = reverse("facilities:create")
        resp = self.client.post(create_url, {
            "name": "UniPod Test Center",
            "location": "Lwera",
            "description": "Testing center",
            "partner_organization": "UniPod",
            "facility_type": Facility.FacilityType.TESTING_CENTER,
            "capabilities": "Materials testing, Compliance",
        }, follow=True)
        self.assertContains(resp, "created successfully")

        obj = Facility.objects.get(name="UniPod Test Center")
        edit_url = reverse("facilities:edit", args=[obj.pk])
        resp = self.client.post(edit_url, {
            "name": "UniPod Test Center V2",
            "location": "Lwera",
            "description": "Updated",
            "partner_organization": "UniPod",
            "facility_type": Facility.FacilityType.TESTING_CENTER,
            "capabilities": "Materials testing, Compliance",
        }, follow=True)
        self.assertContains(resp, "updated successfully")

        delete_url = reverse("facilities:delete", args=[obj.pk])
        resp = self.client.post(delete_url, follow=True)
        self.assertContains(resp, "deleted")
