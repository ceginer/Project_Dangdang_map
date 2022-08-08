from django.urls import path 

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "dang"

urlpatterns = [
  path('', views.home, name='home'),
  path('cafe', views.cafeList, name='cafeList'),
  path('place', views.placeList, name='placeList'),
  path('accomo', views.accomoList, name='accomoList'),
  path('cates/', views.cates, name='cates'), # category 선택 ajax
  path('locationBtn/', views.locationBtn, name='locationBtn'), # 지역 고르기 ajax
  path('listGo/', views.listGo, name='listGo'), # 선택 적용 ajax
  path('cities/<str:location>', views.mainList, name='mainList'),
  path('csvToModel', views.csvToModel, name='csvToModel'),


] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)