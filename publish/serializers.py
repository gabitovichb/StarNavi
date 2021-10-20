from rest_framework import serializers
from .models import *


class ReportSerializer(serializers.ModelSerializer):


    class Meta:
        model = Report
        fields = ['id','title', 'body', 'author']


class ReportListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    count = serializers.SerializerMethodField()


    def get_count(self, obj):
        return len((list(obj.likes.all())))


    class Meta:
        model = Report
        fields = ['id', 'title', 'body', 'created_at', 'author', 'count']