"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import app01.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app01.views.root),
    path('top/', app01.views.top, name='top'),
    path('app01/pattern/<username>/', app01.views.pattern, name='pattern'),
    path('app01/param/', app01.views.param, name='param'),
    path('top/dm', app01.views.dm, name='dm'),
    path('top/tt', app01.views.tt, name='tt'),
    path('login', app01.views.logout, name='logout'),
    path('cla', app01.views.cla, name='cla'),
    path('event', app01.views.logout, name='event'),
    path('osero', app01.views.osero, name='osero'),
    path('home', app01.views.home, name='home'), #login中か確かめるテスト用
]