from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('signin', views.signin, name="signin"),
    path('profile', views.profile, name="profile"),
    path('logout', views.logout, name="logout")

]
