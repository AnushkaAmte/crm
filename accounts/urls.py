from os import name
from django.urls import path
from . import views
import accounts




urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('', views.home, name='home'),
    path('user/',views.userPage,name="user-page"),
    path('account/', views.accountSettings,name="account"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name='customers'),
    
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<str:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),
]

