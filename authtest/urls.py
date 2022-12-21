from django.urls import path
from . import views
#画像
from django.conf import settings
from django.conf.urls.static import static
from app01.views import index

urlpatterns = [
    path('home', views.home, name='home'),
    path('priv', views.private_page, name='priv'),
    path('pub', views.public_page, name='pub'),
    path('signup/', views.signup, name='signup'),
    path('', index, name='top'),
    #path('start/', views.start_page, name='start'),
    path('mypage/', views.mypage, name='mypage'),
    path('chat/', views.mypage, name='chat'),
]

#画像
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)