
from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginPage,name='loginPage'),
    path('signup/', views.signup,name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
]