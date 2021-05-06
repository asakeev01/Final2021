from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import ValidationError 
from django.contrib.auth.models import User

from apps.products.serializers import ProductItemSerializer
from .models import Bookmark


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'bookmark', 'cart')
    

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required= True, validators = [UniqueValidator(queryset = User.objects.all())])
    password1 = serializers.CharField(max_length = 8, write_only = True, label = 'Password', style = {'input_type': 'password'})
    password2 = serializers.CharField(max_length = 8, write_only = True, label = 'Confirm Password', style = {'input_type' : 'password'} )

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password1', 'password2')
    
    def create(request, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password1 = validated_data['password1']
        user = User(username = username, email = email)
        if password1 != validated_data['password2']:
            return ValidationError('passwords do not match')
        else:
            user.set_password(password1)
            user.save()
        return user
        fields = ('url', 'username', 'email', 'bookmark', 'cart')


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    product_items = ProductItemSerializer(many=True)

    class Meta:
        model = Bookmark
        fields = ('user', 'product_items')
