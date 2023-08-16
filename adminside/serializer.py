from rest_framework import serializers
from adminside.models import Categories, ItemImage, Items

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = [
            'id',
            'name',
            'description',
            'image'
        ]
    def create(self, validated_data):
        category=Categories.objects.create(**validated_data)
        return category


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['image']

class ItemsSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)
    class Meta:
        model = Items
        fields = [
            'id',
            'name',
            'in_stock',
            'description',
            'category',
            'images'
        ]
    
    def create(self, validated_data):
        items=Items.objects.create(**validated_data)
        return items