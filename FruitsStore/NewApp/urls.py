from django.contrib import admin
from django.urls import path

from NewApp import views

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('regis/', views.regis, name='regis'),
    path('table/', views.table, name='table'),
    path('tabledata/', views.tabledata, name='tabledata'),
    path('edits/<int:dataid>', views.edits, name='edits'),
    path('update/<int:dataid>', views.update, name='update'),
    path('delete/<int:to>/', views.delete, name='delete'),
    path('addproducts/', views.addproducts, name='addproducts'),
    path('category/', views.category, name='category'),
    path('newcate/', views.newcate, name='newcate'),
    path('catable/', views.catable, name='catable'),
    path('deletedetail/<int:dataid>/', views.deletedetail, name='deletedetail'),
    path('updateedit/<int:up>/', views.updateedit, name='updateedit'),
    path('editupdate/<int:do>/', views.editupdate, name='editupdate'),
    path('contacttable/', views.contacttable, name="contacttable"),
]