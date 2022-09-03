from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('priv', views.private_page, name='priv'),
    path('pub', views.public_page, name='pub'),
    path('signup/', views.signup, name='signup'),
    path('top', views.top_page, name='top'),
]