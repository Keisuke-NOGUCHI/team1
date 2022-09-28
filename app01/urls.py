from django.urls import path
from . import views
#画像
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name='index'),
	path('rank', views.rank, name='rank'),
	path('<int:article_id>/', views.detail, name='detail'),
	path('<int:article_id>/update', views.update, name='update'),
	path('<int:article_id>/delete', views.delete, name='delete'),
	path('<int:article_id>/like',views.like, name='like'),
]
#画像
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)