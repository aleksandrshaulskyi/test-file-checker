from os.path import basename
from pathlib import Path

from rest_framework import serializers

from applications.checker.models import File
from applications.checker.serializers import ListCheckSerializer


class UploadFileSerializer(serializers.ModelSerializer):
    """
    The serializer that is used to upload files.

    Requires only file itself. Everything else is either
    provided in perform_create either automatically.
    """

    id = serializers.IntegerField(read_only=True)
    last_checked_at = serializers.DateTimeField(read_only=True)
    last_check_status = serializers.CharField(read_only=True)
    checks = ListCheckSerializer(many=True, read_only=True)

    class Meta:
        model = File
        fields = ('id', 'file', 'last_checked_at', 'last_check_status', 'checks')

    def validate(self, attrs: dict) -> dict:
        file = attrs.get('file')
        extension = Path(file.name).suffix.lower()

        if extension != '.py':
            raise serializers.ValidationError({'file': 'Unsupported file extension.'})
        
        return attrs
    
    def to_representation(self, instance: File) -> dict:
        representation = super().to_representation(instance=instance)

        representation.update({'file': basename(instance.file.name)})

        return representation
