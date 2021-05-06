from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User


from .serializers import UserSerializer, BookmarkSerializer, UserCreateSerializer

from .models import Bookmark


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer 
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username = user)


        

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer




class BookmarkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer