from django.urls import path
from . import views


urlpatterns = [
    path('passport/', views.passport_list, name='passport_list'),
    path('passport-search/', views.passport_search, name='passport_search'),
    path('passport-search-result/', views.passport_search_result, name='passport_search_result'),
    path('admin-passport/', views.admin_passport_list, name='admin_passport_list'),
    path('passport-create/', views.passport_create, name='passport_create'),
    path('passport-update/<int:passport_id>/', views.passport_update, name='passport_update'),
    path('passport-delete/<int:passport_id>/', views.passport_delete, name='passport_delete'),
    path('passport-verify/<int:passport_id>/', views.admin_passport_verify, name='admin_passport_verify'),
]
