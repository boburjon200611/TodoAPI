from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from Todoapp.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', PlanListAPIView.as_view()),
    path('todo/<int:pk>/', RetriveAPIView.as_view()),
    path('get-token/',TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('get-token/', obtain_auth_token),
]
