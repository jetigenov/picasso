from django.urls import path
from rest_framework import routers

from . import views

app_name = 'police_department'

router = routers.DefaultRouter()
router.register(r'calls', views.CallsViewSet, basename='calls')

urlpatterns = [
    path('', views.upload_csv, name='add'),
]

urlpatterns += router.urls
