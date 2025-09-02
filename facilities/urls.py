from django.urls import path
from . import views

app_name = "facilities"

urlpatterns = [
    path("", views.FacilityListView.as_view(), name="list"),
    path("create/", views.FacilityCreateView.as_view(), name="create"),
    path("<int:pk>/", views.FacilityDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.FacilityUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.FacilityDeleteView.as_view(), name="delete"),
]
