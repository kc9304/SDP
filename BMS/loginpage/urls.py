from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('one/', views.home, name="one"),
    path('two/', views.home2, name="two"),
    path('checklogin/', views.checklogin, name="checklogin"),
    path('base/',views.base,name="base"),
    path('checkbook/', views.checkbook, name="checkbook"),
    path('register/', views.register, name="register"),
    path('addregister/', views.addregister, name="addregister"),
     path('profile/', views.profile, name="profile"),
    path('form/', views.form, name="form"),
    path('addpersonal/', views.addpersonal, name="addpersonal"),
    path('vieworder/', views.vieworder, name="vieworder"),
    path('cart/', views.cart, name="cart"),
    path('contact/', views.contact, name="contact"),

]