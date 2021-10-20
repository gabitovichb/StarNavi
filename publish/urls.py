from django.urls import path, include

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', ReportCreateViewSet, basename='post_create')


urlpatterns = [
    path('', include(router.urls)),
    path('create', ReportCreate.as_view(), name="create_post"),
    path('posts', ReportList.as_view(), name="all_post"),
    path('like', LikeView.as_view(), name='like_post'),
    path('unlike', UnlikeView.as_view(), name='unlike_post'),
    ]
