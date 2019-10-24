from django.shortcuts import render
from items.models import Item, FavoriteItem
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ItemListSerializer, ItemDetailSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsItemOwnerOrStaff


class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name', 'description', 'added_by']
	permission_classes = [AllowAny]

class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [IsAuthenticated, IsItemOwnerOrStaff]
	

# Create your views here.
