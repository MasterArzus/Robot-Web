"""
URL configuration for robot_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from robot_app import views, admin_views, user_views
from django.urls import path

urlpatterns = [
    # login page
    path('', views.loginPage, name="login"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('doRegister/', views.doRegister, name="doRegister"),

    # admin
    path('admin_home/', admin_views.admin_home, name="admin_home"),

    # user
    path('testuser_home/', user_views.testuser_home, name="testuser_home"),
    path('scoring_done/', user_views.scoring_done, name="scoring_done"),
    path('statics/', user_views.statics, name="statics"),


]
