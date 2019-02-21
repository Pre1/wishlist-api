from items.models import Item

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsStaffOrOwner

from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
	CreateAPIView,
)

from .serializers import ItemListSerializer, ItemDetailSerializer

# TODO: impl search & order for ItemListView
from rest_framework.filters import OrderingFilter, SearchFilter


class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	filter_backends = [OrderingFilter, SearchFilter,]
	search_fields = ['name', 'description',]
	permission_classes = [AllowAny,]


class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [IsAuthenticated, IsStaffOrOwner,]
