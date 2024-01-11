from rest_framework.serializers import ModelSerializer

from .models import Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ["art_number", "description", "original_price", "price", "ean_code", "image_name", "image_url"]
