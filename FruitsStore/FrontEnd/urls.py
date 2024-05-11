from django.contrib import admin
from django.urls import path,include

from FrontEnd import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('filterproduct/<cat>/', views.filterproduct, name='filterproduct'),
    path('singleproduct/<int:data>/', views.singleproduct, name='singleproduct'),
    path('productpage/', views.productpage, name='productpage'),
    path('signuppage/', views.signuppage, name='signuppage'),
    path('savelog/', views.savelog, name='savelog'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('loginsave/', views.loginsave, name='loginsave'),
    path('contact/', views.contact, name='contact'),
    path('contactdata/', views.contactdata, name='contactdata'),
    path('cart/', views.cart, name='cart'),
    path('cartdata/', views.cartdata, name='cartdata')
]