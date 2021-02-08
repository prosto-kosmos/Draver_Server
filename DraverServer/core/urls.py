from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index_view.as_view(), name='index_url'),
    path('api/log/connect/', views.api_connect_view),
    path('api/log/insert/', views.api_insert_view),
]