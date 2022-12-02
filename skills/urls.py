from django.urls import path
from . import views


urlpatterns = [
    path('admin-skill/', views.admin_skills_list, name='admin_skill_list'),
    path('skill/', views.skills_list, name='skill_list'),
    path('skill-create/', views.skills_create, name='skill_create'),
    path('skill-delete/<int:skill_id>/', views.skill_delete, name='skill_delete'),
    path('skill-update/<int:skill_id>/', views.skill_update, name='skill_update'),
]
