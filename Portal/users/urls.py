"""Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path("login/", views.user_Portal),
    # path("data/", views.user_data),
    path("signup/", views.signupF),
    # path("login/", views.loginPage),
    path("profile_info/", views.profile),
    path("profile_addr/", views.address),
    path("upload_profile/", views.upload_profile),
    path("update_username/<id>", views.update_username),
    path("upload_profile/", views.upload_profile),
    # path("profile_ph/", views.phone),
    # path("update_ph/<int:id>", views.update_ph),
    path("update_addr/<int:id>", views.update_addr),
    path("delete_addr/<int:id>", views.delete_addr),
    path("showdata/", views.Display_data),
]
