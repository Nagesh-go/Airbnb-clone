from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, PropertyImageViewSet, ReviewViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'images', PropertyImageViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
] 