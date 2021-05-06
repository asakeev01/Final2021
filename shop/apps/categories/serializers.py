from rest_framework import serializers
from .models import Category
from rest_framework_recursive.fields import RecursiveField


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        model = Category
        fields = ('url', 'id', 'title', 'children', 'products', 'parent')


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'parent')
