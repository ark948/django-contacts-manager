from django.urls import path
from apps.accounts.api.views import UserList, UserDetail

app_name = "accounts_api"
urlpatterns = [
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetail().as_view(), name="user_detail"),
]