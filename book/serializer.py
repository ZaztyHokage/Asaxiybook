from rest_framework import serializers

from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1

    def get_genre(self, obj):
        data = []
        for genre in obj.genre.all():
            data.append({
                'id': genre.id,
                'name': genre.name
            })
        return data
    
    def get_tag(self, obj):
        data = []
        for tag in obj.tag.all():
            data.append({
                'id': tag.id,
                'name': tag.name
            })
        return data
