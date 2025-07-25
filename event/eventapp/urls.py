from django.urls import path
from eventapp.views import *



urlpatterns = [
    path("register/",UserRegistation.as_view(),name="register"),
    path("events/",EventCreateListView.as_view(),name="events"),
    path("events/<int:pk>",EventUpdateDeleteView.as_view(),name="eventspk")
]
