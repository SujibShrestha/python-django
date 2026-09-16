from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_app, name='all_app'),
    path('<int:app_id>/',views.app_detail, name='app_detail'),
    path('stores/', views.stores, name='stores')

] 