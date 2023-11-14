from rest_framework import serializers


from rest_framework.renderers import JSONRenderer
import rest_framework

from .models import Book


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)
    description = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.save()
        return instance
