from django.urls import path
from contactlist.views import *


urlpatterns = [

    path("register/",UserRegisterView.as_view(),name="register"),
    path("contactlists/",ConatctListCreate.as_view(),name="list"),
    path("contact/<int:pk>",ContactDeletUpdateView.as_view(),name="contactsingle"),
    path("favcontact/",FavoriteContactView.as_view(),name="favcontactlist")
]