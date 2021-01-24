from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('adminsignin/', views.admin_sign_in, name='admin_sign_in'),
    path('adminhome/', views.admin_home, name='admin_home'),
    path('adminlogout/', views.admin_logout, name='admin_logout'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
]
