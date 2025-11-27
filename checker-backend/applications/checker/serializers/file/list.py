from os.path import basename

from rest_framework import serializers

from applications.checker.models import File
from applications.checker.serializers import ListCheckSerializer


class ListFileSerializer(serializers.ModelSerializer):

    last_checked_at = serializers.DateTimeField(format='%H:%M:%S')
    checks = ListCheckSerializer(many=True)

    class Meta:
        model = File
        fields = ('id', 'file', 'last_checked_at', 'last_check_status', 'checks')

    def to_representation(self, instance: File) -> dict:
        representation = super().to_representation(instance=instance)

        representation.update({'file': basename(instance.file.name)})

        return representation
