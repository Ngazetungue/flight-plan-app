from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView 

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Trip
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'travel/index.html'
    

class DestinationPageView(TemplateView):
    template_name = 'travel/destination.html'

class PricingPageView(TemplateView):
    template_name = 'travel/pricing.html'

class ContactPageView(TemplateView):
    template_name = 'travel/contact.html'

class TravelListView(LoginRequiredMixin,ListView):
    model = Trip
    context_object_name = 'trip_list'
    template_name = 'travel/travel_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trip_list'] = context['trip_list'].filter(author=self.request.user)
        return context

class TravelDetailView(LoginRequiredMixin,DetailView):
    model = Trip
    context_object_name = 'trip_detail'
    template_name = 'travel/travel_detail.html'

class TravelCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    template_name = 'travel/travel_create.html'
    fields = ('country', 'destination', 'start', 'end', 'activity',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TravelUpdateView(UpdateView): 
    model = Trip
    template_name = 'travel/travel_edit.html'
    fields = ['start', 'end', 'activity']

class TravelDeleteView(DeleteView):
    model = Trip
    template_name = 'travel/travel_delete.html'
    success_url = reverse_lazy('travellist')