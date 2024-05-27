from django.urls import path
from apps.contacts.api.views import ContactList, ContactDetail

urlpatterns = [
    path("<int:pk>/", ContactDetail.as_view(), name="contact_detail"),
    path("", ContactList.as_view(), name="contact_list"),
]