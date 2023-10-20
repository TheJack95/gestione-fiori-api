from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Item
from .serializers import ItemSerializer


# Create your views here.
class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
