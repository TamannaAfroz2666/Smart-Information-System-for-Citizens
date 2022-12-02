from django.urls import path
from . import views


urlpatterns = [
    path('education-list-search/', views.education_list_search, name='education_list_search'),
    path('education-list-search-result/', views.education_list_search_result, name='education_list_search_result'),
    path('education-list/', views.education_list, name='education_list'),
    path('admin-education/', views.admin_education_list, name='admin_education_list'),
    path('education-create/', views.education_create, name='education_create'),
    path('education-update/<int:education_id>/', views.education_update, name='education_update'),
    path('education-delete/<int:education_id>/', views.education_delete, name='education_delete'),
]
