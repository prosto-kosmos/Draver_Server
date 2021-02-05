from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index_view.as_view(), name='index_url'),
    path('api/log/connect/', views.Api_connect_view.as_view(), name='api_connect_url'),
    path('api/log/insert/', views.Api_insert_view.as_view(), name='api_insert_url'),
    # path('calculation/', views.Calc_view.as_view(), name='calculation_url'),
    # path('grath/', views.Grath_view.as_view(), name='grath_url'),
    # path('analysis/', views.Analysis_view.as_view(), name='analysis_url'),
]