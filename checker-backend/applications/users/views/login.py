from http import HTTPStatus

from django.contrib.auth import login
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.users.serializers import LoginSerializer


class LoginAPIView(APIView):
    """
    A simple view to log a user in.
    """

    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        if (user := serializer.context.get('user')) is not None:
            login(request=request, user=user)
            return Response(status=HTTPStatus.OK)

        return Response(status=HTTPStatus.BAD_REQUEST)
