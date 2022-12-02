from django.urls import path
from . import views


urlpatterns = [
    path('admin-experience/', views.admin_experience_list, name='admin_experience_list'),
    path('experience/', views.experience_list, name='experience_list'),
    path('experience-create/', views.experience_create, name='experience_create'),
    path('experience-update/<int:experience_id>/', views.experience_update, name='experience_update'),
    path('experience-delete/<int:experience_id>/', views.experience_delete, name='experience_delete'),
]
