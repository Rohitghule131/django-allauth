from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
from rest_framework.response import Response

from .models import Auther
from utilities.utils import ResponseInfo
from .serializers import ListAutherSerializer


class LoginRedirectAPIView(RetrieveAPIView):
    """
    Class for create to redirect url once user successfully login.
    """
    serializer_class = ()
    permission_classes = ()
    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        """
        Method for return response once user login.
        """
        print("USER<><><", request.user, request.data, request.headers)
        return Response({"SUCCESS": "User successfully login."})


class LogoutRedirectAPIView(RetrieveAPIView):
    """
    Class for create to redirect url once user successfully logout.
    """
    serializer_class = ()
    permission_classes = ()
    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        """
        Method for return response once user login.
        """

        print(request)
        print("USER<><><", request.user)
        return Response({"SUCCESS": "User successfully logout."})


class ListAutherAPIView(ListAPIView):
    """
    Class for creation list api.
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = ListAutherSerializer

    def __init__(self, **kwargs):
        """
        Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(ListAutherAPIView, self).__init__(**kwargs)

    def get_queryset(self):
        """
        Method for get all auther.
        """
        return Auther.objects.all().order_by("created_at")

    def get(self, request, *args, **kwargs):
        """
        GET method for a return auther list.
        """
        print(request.headers)
        auther_serializer = super().list(request, *args, **kwargs)

        self.response_format["data"] = auther_serializer.data
        self.response_format["status_code"] = status.HTTP_200_OK
        self.response_format["error"] = None
        self.response_format["message"] = ["Success."]

        return Response(self.response_format)
