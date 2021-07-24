from django.urls import path
from .views import (
    HomePageView, 
    TravelListView, 
    TravelDetailView,
    TravelCreateView,
    TravelUpdateView,
    TravelDeleteView,
    
)
urlpatterns = [
    path('', HomePageView.as_view(), name='home' ),
    path('travellist/', TravelListView.as_view(), name="travellist"),
    path('<int:pk>', TravelDetailView.as_view(), name="travel_detail"),
    path('create/', TravelCreateView.as_view(), name="travel_create"),
    path('trip/<int:pk>/edit/', TravelUpdateView.as_view(), name="travel_edit"),
    path('trip/<int:pk>/delete/', TravelDeleteView.as_view(), name="travel_delete"),
    


]
