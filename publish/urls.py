from django.urls import path, include

from .views import ReportCreate, ReportList, LikeView, UnlikeView, PostAnaliticsLikesView


urlpatterns = [
    path('create', ReportCreate.as_view(), name="create_post"),
    path('all', ReportList.as_view(), name="all_post"),
    path('like', LikeView.as_view(), name='like_post'),
    path('unlike', UnlikeView.as_view(), name='unlike_post'),
    path('analitics/', PostAnaliticsLikesView.as_view(), name='post_likes')
    ]
