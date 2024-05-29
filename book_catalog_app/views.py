from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets


from .models import *
from .serializers import *

# Create your views here.

class BookGenreViewSet(viewsets.ModelViewSet):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer

class BookViewSet(viewsets.ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
   queryset = Author.objects.all()
   serializer_class = AuthorSerializer

class RatingViewSet(viewsets.ModelViewSet):
   queryset = Rating.objects.all()
   serializer_class = RatingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
   queryset = Review.objects.all()
   serializer_class = ReviewSerializer

# Because I put 'IsAuthenticated' in this get, only the superuser can access stuff, so you need to log in to get your token
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
   user = request.user
   profile = user.profile
   serialized_profile = ProfileSerializer(profile)
   return Response(serialized_profile.data)



@api_view(['POST'])
@permission_classes([])
def create_user(request):
   user = User.objects.create(
       username = request.data['username'],
   )
   user.set_password(request.data['password'])
   user.save()
   profile = Profile.objects.create(
       user = user,
       first_name = request.data['first_name'],
       last_name = request.data['last_name']
   )
   profile.save()
   profile_serialized = ProfileSerializer(profile)
   return Response(profile_serialized.data)
   
