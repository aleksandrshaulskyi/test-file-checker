from django.db.models import QuerySet
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet

from applications.checker.choices import FileStatus
from applications.checker.models import Check, File
from applications.checker.serializers import ListFileSerializer, UpdateFileSerializer, UploadFileSerializer
from applications.checker.tasks import check


class FileViewSet(ModelViewSet):

    def get_permissions(self) -> list[BasePermission]:
        permissions_map = {
            'list': [IsAuthenticated],
            'create': [IsAuthenticated],
            'partial_update': [IsAuthenticated]
        }

        self.permission_classes = permissions_map.get(self.action, [IsAuthenticated])

        return super().get_permissions()

    def get_queryset(self) -> QuerySet:
        return File.objects.filter(user=self.request.user).prefetch_related('checks')
    
    def get_serializer_class(self) -> Serializer | None:
        serializers_map = {
            'list': ListFileSerializer,
            'create': UploadFileSerializer,
            'partial_update': UpdateFileSerializer,
        }

        return serializers_map.get(self.action)
    
    def perform_create(self, serializer: Serializer) -> None:
        file = serializer.save(
            user=self.request.user,
        )

        check.delay(file.id)

    def perform_update(self, serializer: Serializer) -> File:
        instance = serializer.save(
            last_check_status=FileStatus.CHECK_PENDING,
        )

        Check.objects.filter(file=instance).delete()

        check.delay(instance.id)

        return instance
