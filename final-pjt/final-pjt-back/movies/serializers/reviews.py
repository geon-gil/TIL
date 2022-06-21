from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Review
from .comments import CommentListSerializer
User = get_user_model()


class ReviewListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    comment_set = CommentListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Review
        fields = (
            'pk',
            'user',
            'movie',
            'title',
            'content',
            'created_at',
            'updated_at',
            'like_users',
            'not_like_users',
            'comment_set',
        )
        read_only_fields = ('movie', 'like_users', 'not_like_users', )