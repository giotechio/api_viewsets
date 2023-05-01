from rest_framework import generics, permissions
from .models import Posting
from .serializers import PostingSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsCreatorOrReadOnly

from rest_framework.decorators import api_view 
from rest_framework.response import Response  
from rest_framework.reverse import reverse  


# root endpoint

@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "postings": reverse("posting-list", request=request, format=format),
        }
    )


# ListCreateAPIView to create a read-write endpoint that lists all available 'Posting' instances

class PostingList(generics.ListCreateAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


# RetrieveUpdateDestroyAPIView for a read-write-delete endpoint for each individual Posting
class PostingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsCreatorOrReadOnly,)


# Users 

class UserList(generics.ListAPIView):  
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):  
    queryset = User.objects.all()
    serializer_class = UserSerializer