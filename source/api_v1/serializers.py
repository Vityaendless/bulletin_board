from rest_framework import serializers
from webapp.models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            'id', 'photo', 'title', 'description',
            'author', 'category', 'price', 'status',
            'published_at', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'photo', 'title', 'description',
            'author', 'category', 'price', 'status',
            'published_at', 'created_at', 'updated_at'
        ]

