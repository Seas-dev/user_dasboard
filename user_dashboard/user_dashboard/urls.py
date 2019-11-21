"""user_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from apps.login_app import views as login_views
from apps.dashboard_app import views as dash_views

urlpatterns = [
    path('', login_views.index),
    path('signin', login_views.signin),
    path('logout', login_views.logout),
    path('register', login_views.register),
    path('createUser', login_views.createUser),
    path('loginUser', login_views.loginUser),
    path('whichDash', dash_views.whichDash),
    path('adminDash', dash_views.adminDash),
    path('dashboard', dash_views.dashboard),
    path('users/new', dash_views.adminAddNew),
    path('deleteUser/<id>', dash_views.deleteUser),
    path('editUser/<id>', dash_views.editUser),
    path('users/edit/<id>', dash_views.adminEditUser),
    path('users/edit', dash_views.editProfile),
    path('editDesc', dash_views.editDesc),
    path('users/show/<id>', dash_views.showUser),
    path('createPost/<id>', dash_views.createPost),
    path('createComment/<messageID>', dash_views.createComment),
    path('admin/', admin.site.urls),
]
