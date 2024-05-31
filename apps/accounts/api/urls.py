from django.urls import path
from apps.accounts.api.views import UserList, UserDetail, UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"users", UserViewSet)

urlpatterns = router.urls