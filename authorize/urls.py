from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token

from .views import *


urlpatterns = [
    path('signup/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('refresh/', refresh_jwt_token),
    ]
