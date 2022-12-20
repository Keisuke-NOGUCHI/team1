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
	#コメント機能
	path('comment/<int:comment_id>/',views.comment_detail, name='comment_detail'),
	path('comment/<int:comment_id>/delete', views.comment_delete, name='comment_delete'),
	path('comment/<int:comment_id>/update', views.comment_update, name='comment_update'),
	path('comment/<int:comment_id>/like',views.comment_like, name='comment_like'),
	#path('<int:article_id>/comment<int:comment_id>/', views.comment_update, name='comment_update'),
]
#画像
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)