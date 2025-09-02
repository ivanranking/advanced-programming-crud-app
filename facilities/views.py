from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Facility
from .forms import FacilityForm
from .filters import filter_facilities

class FacilityListView(ListView):
    model = Facility
    template_name = "facilities/facility_list.html"
    context_object_name = "facilities"
    paginate_by = 10

    def get_queryset(self):
        qs = Facility.objects.all()
        qs = filter_facilities(qs, self.request.GET)
        order = self.request.GET.get("sort", "name")
        allowed = { "name", "-name", "location", "-location", "created_at", "-created_at" }
        if order in allowed:
            qs = qs.order_by(order)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "q": self.request.GET.get("q", ""),
            "type": self.request.GET.get("type", ""),
            "partner": self.request.GET.get("partner", ""),
            "location": self.request.GET.get("location", ""),
            "capability": self.request.GET.get("capability", ""),
            "sort": self.request.GET.get("sort", "name"),
            "types": Facility.FacilityType.choices,
        })
        return ctx

class FacilityDetailView(DetailView):
    model = Facility
    template_name = "facilities/facility_detail.html"
    context_object_name = "facility"

class FacilityCreateView(CreateView):
    model = Facility
    form_class = FacilityForm
    template_name = "facilities/facility_form.html"
    success_url = reverse_lazy("facilities:list")

    def form_valid(self, form):
        messages.success(self.request, "Facility created successfully.")
        return super().form_valid(form)

class FacilityUpdateView(UpdateView):
    model = Facility
    form_class = FacilityForm
    template_name = "facilities/facility_form.html"
    success_url = reverse_lazy("facilities:list")

    def form_valid(self, form):
        messages.success(self.request, "Facility updated successfully.")
        return super().form_valid(form)

class FacilityDeleteView(DeleteView):
    model = Facility
    template_name = "facilities/facility_confirm_delete.html"
    success_url = reverse_lazy("facilities:list")

    # Placeholder for safeguards: When Projects/Equipment/Services are implemented,
    # you may override delete() to block deletion if related records exist.
    # For Week 1–2 scope, direct delete is allowed.
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Facility deleted.")
        return super().delete(request, *args, **kwargs)
