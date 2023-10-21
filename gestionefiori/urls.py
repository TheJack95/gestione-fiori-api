from django.urls import path

from .views import ItemApiView, ItemDetailAPIView

urlpatterns = [
    path("items/",
         ItemApiView.as_view(),
         name="item-list"),
    path("items/<int:pk>/",
         ItemDetailAPIView.as_view(),
         name="item-detail"),
]
