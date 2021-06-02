from django.urls import path
from .views import LoginView, LogoutView, RegisterView,HomePage,CreateSheet, UpdateSheet
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',LoginView.as_view(),name="login"),
    path('register/',RegisterView.as_view(),name="register"),
    path('home/',login_required(HomePage.as_view()),name="home"),
    path('createsheet/',login_required(CreateSheet.as_view()),name="createsheet"),
    path('updatesheet/',login_required(UpdateSheet.as_view()),name="updatesheet"),
    path('logout/',LogoutView.as_view(),name="logout")
]