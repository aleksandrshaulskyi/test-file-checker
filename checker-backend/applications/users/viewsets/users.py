







from http import HTTPStatus

from django.contrib.auth.models import User
from django.db.models import QuerySet
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from applications.users.serializers import RegisterSerializer
from applications.users.services import ValidateTokenService
from applications.users.tasks import generate_link


class CreateUserViewSet(CreateModelMixin, GenericViewSet):
    """
    The viewset that is responsible for the user creation.
    """

    def get_queryset(self) -> QuerySet:
        return User.objects.all()
    
    def get_serializer_class(self) -> Serializer:
        serializers_map = {
            'create': RegisterSerializer,
        }

        return serializers_map.get(self.action)
    
    def perform_create(self, serializer: Serializer) -> None:
        instance = serializer.save()

        generate_link.delay(instance.id)

    @action(detail=False, methods=['GET'], url_path='verify-email')
    def verify_email(self, request: Request) -> Response:
        uid = request.GET.get('uid')
        token = request.GET.get('token')

        if not any([uid, token]):
            return Response(status=HTTPStatus.BAD_REQUEST)
        
        try:
            ValidateTokenService(uid=uid, token=token).execute()
        except Exception:
            return Response(status=HTTPStatus.BAD_REQUEST)
        return Response(status=HTTPStatus.OK)
