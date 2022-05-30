"""ourservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from master.views import MasterViewSet
from booking.views import ApartmentViewSet
from erkindik.views import ArtViewSet, ArtistViewSet
from aviasatuu.views import FlightViewSet, PassengerViewSet
from users import views as user_views


router = routers.DefaultRouter()
router.register(r'masters', MasterViewSet)
router.register(r'booking/apartments', ApartmentViewSet)
router.register(r'erkindik/arts', ArtViewSet)
router.register(r'erkindik/artists', ArtistViewSet)
router.register(r'aviasatuu/passengers', PassengerViewSet)
router.register(r'aviasatuu/flights', FlightViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/user', user_views.user, name='user'),
    path('api/login', user_views.issue_token, name='issue_token'),
    path('api/registration', user_views.UserRegistrationAPIView.as_view(), name='registration')
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
