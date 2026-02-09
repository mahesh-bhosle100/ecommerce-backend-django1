from rest_framework.routers import DefaultRouter
from .views import SignupViewSet, LoginViewSet, ProfileViewSet, ChangePasswordViewSet

router = DefaultRouter()
router.register(r'signup', SignupViewSet, basename='signup')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'change-password', ChangePasswordViewSet, basename='change-password')

urlpatterns = router.urls
