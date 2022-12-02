from django.urls import path
from .views import *


urlpatterns = [
    path('admin_nid_list/', admin_nid_list, name='admin_nid_list'),
    path('nid_list/', nid_list, name='nid_list'),
    path('nid-list-search/', nid_list_search, name='nid_list_search'),
    path('nid-list-search-result/', nid_list_search_result, name='nid_list_search_result'),
    path('nid_create/', nid_create, name='nid_create'),
    path('nid_update/<int:nid_id>/', nid_update, name='nid_update'),
    path('nid_delete/<int:nid_id>/', nid_delete, name='nid_delete'),
    path('admin_nid_verified/<int:nid_id>/', admin_nid_verified, name='admin_nid_verified'),
]
