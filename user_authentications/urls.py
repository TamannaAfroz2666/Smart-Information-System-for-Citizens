from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.registration, name='registration'),
    path('logout/', views.user_logout, name='logout'),
    path('change-password/', views.user_password_change, name='change_password'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('home/', views.user_home, name='user_home'),
    path('search/', views.search_nid, name="search_nid"),
    path('dataTable/', views.dataTableView, name='dataTableView')
]
