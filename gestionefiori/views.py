from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item
from .serializers import ItemSerializer


# Create your views here.
class ItemApiView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        ean_code = request.data.get("ean_code")
        if ean_code is not None:
            item = Item.objects.get(ean_code=ean_code)
            serializer = ItemSerializer(item, data=request.data)
        else:
            serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailAPIView(APIView):
    def get_object(self, ean_code):
        return get_object_or_404(Item, ean_code=ean_code)

    def get(self, request, ean_code):
        item = self.get_object(ean_code)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, ean_code):
        item = self.get_object(ean_code)
        serializer = ItemSerializer(item, data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ean_code):
        item = self.get_object(ean_code)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
