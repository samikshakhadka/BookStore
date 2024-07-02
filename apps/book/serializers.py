from rest_framework import serializers
from .models import Book, Favorite

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['created_by'] = request.user
        return super().create(validated_data)

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'book']
        read_only_fields = ['user']

class SoftDeleteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id']
    
    def update(self, instance, validated_data):
        instance.delete()
        return instance