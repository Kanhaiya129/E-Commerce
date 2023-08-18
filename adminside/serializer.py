from rest_framework import serializers
from adminside.models import Categories, ItemImage, Items


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ["image"]


class ItemsSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = Items
        fields = ["id", "name", "in_stock", "description", "category", "images"]


class CategoriesSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    def get_items(self, obj):
        items=Items.objects.filter(category__id=obj.id)
        serialized_data = ItemsSerializer(items, many=True).data
        return serialized_data


    class Meta:
        model = Categories
        fields = ["id", "name", "description", "image", "items"]

    def create(self, validated_data):
        category = Categories.objects.create(**validated_data)
        return category
