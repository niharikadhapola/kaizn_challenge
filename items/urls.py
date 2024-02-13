from django.urls import path
from items.views import ItemListAPIView, ItemCreateAPIView

urlpatterns = [
    path('items/', ItemListAPIView.as_view(), name='item-list'),
    path('items_create/', ItemCreateAPIView.as_view(), name='item-create'),
]
