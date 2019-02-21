from django.urls import path
from .views import ItemListView, ItemDetailView


urlpatterns = [
	path('list/', ItemListView.as_view(), name='api-list'),
	path('detail/<int:item_id>/', ItemDetailView.as_view(), name='api-detail'),
]