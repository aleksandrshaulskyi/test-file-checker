from rest_framework import serializers

from applications.checker.models import Check


class ListCheckSerializer(serializers.ModelSerializer):

    datetime = serializers.DateTimeField(format='%H:%M:%S')

    class Meta:
        model = Check
        fields = ('status', 'datetime', 'results')

    def to_representation(self, instance: Check) -> dict:
        representation = super().to_representation(instance=instance)

        representation.update({'status': instance.get_status_display()})

        return representation
