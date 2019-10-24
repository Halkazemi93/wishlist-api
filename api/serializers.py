from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']

class ItemListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = 'item-api-detail',
		lookup_field = 'id',
		lookup_url_kwarg = 'item_id'
		)
	added_by = UserSerializer()
	total_favorited = serializers.SerializerMethodField()
	class Meta:
		model = Item 
		fields = ['name', 'description', 'added_by', 'detail', 'total_favorited']

	def get_total_favorited(self, obj):
		total_favorited = obj.favoriteitem_set.all()
		return len(total_favorited)
		# FavoriteItem.objects.filter(item=obj)

	
class ItemDetailSerializer(serializers.ModelSerializer):
	users_who_liked_item = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['id', 'name', 'description', 'users_who_liked_item']

	def get_users_who_liked_item(self, obj):
		obj_list = obj.favoriteitem_set.all()
		users_who_liked_item = []
		for users in obj_list:
			users_who_liked_item.append(users.user)
		return UserSerializer(users_who_liked_item, many=True).data
