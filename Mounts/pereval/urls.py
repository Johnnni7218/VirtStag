from django.urls import path, include
from .views import MountViewSet, MailViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mount', MountViewSet, basename='mount')
router.register(r'email', MailViewSet, basename='email')

urlpatterns = [
    path('submitData/', include(router.urls)),
    path('submitData/?user__email=<email>', include(router.urls)),
]

