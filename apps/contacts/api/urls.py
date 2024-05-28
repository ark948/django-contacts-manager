from django.urls import path
from apps.contacts.api.views import ContactsList, ContactDetail

app_name="contact_api"
urlpatterns = [
    path("<int:pk>/", ContactDetail.as_view(), name="contact_detail"),
    path("", ContactsList.as_view(), name="contact_list"),
]