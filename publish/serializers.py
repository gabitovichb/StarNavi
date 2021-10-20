from rest_framework import serializers
from .models import Report, Like, Dislike


class ReportSerializer(serializers.ModelSerializer):


    class Meta:
        model = Report
        fields = ['id','title', 'body', 'author']


class ReportListSerializer(ReportSerializer):
    author = serializers.ReadOnlyField(source='author.username')


    class Meta(ReportSerializer.Meta):
        fields = ReportSerializer.Meta.fields + ['created_at' ,'author']


class LikeSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Like
        fields = ('like_author', 'like_post', 'like', 'like_created')


class DislikeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Dislike
        fields = ('dislike_author', 'dislike_post', 'dislike', 'dislike_created')