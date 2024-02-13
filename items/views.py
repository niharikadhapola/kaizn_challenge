from rest_framework import generics, pagination
from .models import Item
from items.permissions import IsAuthenticatedForItemsApp
from .serializers import ItemSerializer

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10  # Adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedForItemsApp]
    pagination_class = CustomPagination
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtering by in_stock
        in_stock = self.request.query_params.get('in_stock', None)
        if in_stock:
            queryset = queryset.filter(in_stock=in_stock)

        # Filtering by available_stock
        available_stock = self.request.query_params.get('available_stock', None)
        if available_stock:
            queryset = queryset.filter(available_stock=available_stock)

        # Filtering by stock_status
        stock_status = self.request.query_params.get('stock_status', None)
        if stock_status:
            queryset = queryset.filter(stock_status=stock_status)

        return queryset

class ItemCreateAPIView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedForItemsApp] 
