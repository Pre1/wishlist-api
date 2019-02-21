from items.models import Item, FavoriteItem
from rest_framework import serializers
from items.models import Item

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name']


class FavItemSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = FavoriteItem
		fields = ['user']
		

class ItemListSerializer(serializers.ModelSerializer):
	
	detail = serializers.HyperlinkedIdentityField( 
		view_name = "api-detail",
		lookup_field = "id",
		lookup_url_kwarg = "item_id",
	)

	added_by = UserSerializer()

	total_favs = serializers.SerializerMethodField()
	# users = FavItemSerializer(many = True)
	class Meta:
		model = Item
		fields = [
			'id',
			'name',
			'detail',
			'added_by',
			'total_favs',
			]

	def get_total_favs(self, obj):
		favs = obj.items.all()
		favs_ser = FavItemSerializer(favs, many = True)
		return len(favs_ser.data)


class ItemDetailSerializer(serializers.ModelSerializer):

	# items = FavItemSerializer(many = True)
	# users_d = serializers.PrimaryKeyRelatedField(queryset=Item.users.get('username'))
	# users_d = FavItemSerializer(many = True, queryset=User.objects.all())

	print("===========================")
	# print("user: ", users_d)
	# print("type: ", dir(users_d))
	# print('Item.users.all(): ', vars(Item.users.field))

	users_fav = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = [
			'image',
			'name',
			'description',
			'users_fav',
			]

	def get_users_fav(self, obj):
		favs = obj.items.all()
		items = FavItemSerializer(favs, many = True)
		return items.data
