from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name = 'login'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name = 'logout'),
    path('loans/', views.loans, name='loans'),
    path('transactions/', views.transactions, name='transactions'),
]