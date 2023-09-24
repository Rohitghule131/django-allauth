from django.urls import path
from .views import (
    ListAutherAPIView,
    LoginRedirectAPIView,
    LogoutRedirectAPIView,
)

urlpatterns = [
    path("loginRedirectURL", LoginRedirectAPIView.as_view(), name="login-redirect-URL"),
    path("logoutRedirectURL", LogoutRedirectAPIView.as_view(), name="logout-redirect-URL"),

    path("listAuther", ListAutherAPIView.as_view(), name="list-auther"),
]
