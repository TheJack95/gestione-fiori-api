from django.urls import path

from .views import ItemApiView, ItemDetailAPIView

urlpatterns = [
    path("items/",
         ItemApiView.as_view(),
         name="item-list"),
    path("items/<str:ean_code>/",
         ItemDetailAPIView.as_view(),
         name="item-detail"),
]
