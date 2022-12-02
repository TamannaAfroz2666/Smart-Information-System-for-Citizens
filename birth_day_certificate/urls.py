from django.urls import path
from . import views


urlpatterns = [
    path('admin-birth-day-certificate/', views.admin_birthday_certificate_list, name='admin_birth_day_certificate_list'),
    path('admin-birth-day-certificate-verified/<int:birth_day_certificate_id>/', views.birth_day_certificate_verified,
         name='birth_day_certificate_verified'),
    path('birth-day-certificate/', views.birthday_certificate_list, name='birth_day_certificate_list'),
    path('birth-day-certificate-search/', views.birthday_certificate_search, name='birth_day_certificate_search'),
    path('birth-day-certificate-search-result/', views.birthday_certificate_search_result,
         name='birthday_certificate_search_result'),
    path('birth-day-certificate-create/', views.birthday_certificate_create, name='birth_day_certificate_create'),
    path('birth-day-certificate-update/<int:birth_day_certificate_id>/', views.birth_day_certificate_update,
         name='birth_day_certificate_update'),
    path('birth-day-certificate-delete/<int:birth_day_certificate_id>/', views.birth_day_certificate_delete,
         name='birth_day_certificate_delete'),
]
