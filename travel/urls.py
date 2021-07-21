from django.urls import path
from .views import (
    HomePageView, 
    DestinationPageView, 
    PricingPageView, 
    ContactPageView, 
    TravelListView, 
    TravelDetailView,
    TravelCreateView,
    TravelUpdateView,
    TravelDeleteView,
    
)
urlpatterns = [
    path('', HomePageView.as_view(), name='home' ),
    path('destination/', DestinationPageView.as_view(), name='destination'),
    path('pricing/', PricingPageView.as_view(), name='pricing'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('travellist/', TravelListView.as_view(), name="travellist"),
    path('<int:pk>', TravelDetailView.as_view(), name="travel_detail"),
    path('create/', TravelCreateView.as_view(), name="travel_create"),
    path('trip/<int:pk>/edit/', TravelUpdateView.as_view(), name="travel_edit"),
    path('trip/<int:pk>/delete/', TravelDeleteView.as_view(), name="travel_delete"),
    


]
