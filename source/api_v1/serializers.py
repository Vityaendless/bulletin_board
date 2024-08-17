from django.shortcuts import get_object_or_404, redirect
from rest_framework import serializers

from webapp.models import Comment, Ad


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'ad', 'created_at', 'updated_at')
        read_only_fields = ['author', 'ad']

    def to_internal_value(self, data):
        internal_value = super(CommentModelSerializer, self).to_internal_value(data)
        ad = data.get("ad")
        internal_value.update({
            "ad": ad
        })
        return internal_value

    def create(self, validated_data):
        self.to_internal_value(validated_data)
        ad_object = get_object_or_404(Ad, pk=validated_data['ad'])
        validated_data['ad'] = ad_object
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)
