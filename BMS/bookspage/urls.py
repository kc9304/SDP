from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('main/', views.main, name="main"),
    path('cone/', views.one, name="cone"),
    path('ctwo/',views.two,name="ctwo"),
    path('vol1/', views.vol1, name="vol1"),
    path('vol2/', views.vol2, name="vol2"),
    path('vol3/', views.vol3, name="vol3"),
    path('vol4/', views.vol4, name="vol4"),
    path('vol5', views.vol5, name="vol5"),
    path('vol6/', views.vol6, name="vol6"),
    path('vol7/', views.vol7, name="vol7"),
    path('vol8/', views.vol8, name="vol8"),
    path('vol9/', views.vol9, name="vol9"),
    path('vol10/', views.vol10, name="vol10"),
    path('success/', views.success, name="success"),
    path('kc/', views.kc, name="kc"),
    path('cart1/', views.cart1, name="cart1"),

    path('cart2/', views.cart2, name="cart2"),

    path('cart3/', views.cart3, name="cart3"),

    path('cart4/', views.cart4, name="cart4"),

    path('cart5/', views.cart5, name="cart5"),

]