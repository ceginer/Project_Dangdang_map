from django.urls import path 

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "dang"

urlpatterns = [
  path('', views.home, name='home'),
  path('cafe',views.cafeList, name='cafeList'),
  path('accomodation', views.accomodationList, name='accomodationList'),
  path('place', views.placeList, name='placeList'),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)