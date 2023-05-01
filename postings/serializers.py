from rest_framework import serializers
from .models import Posting
from django.contrib.auth.models import User

# serializer using Hyperlink

class PostingSerializer(serializers.HyperlinkedModelSerializer):

    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        model = Posting
        fields = (
            'url',
            'id', 
            'title',
            'contents',
            'creator',
            )

# user serialiser with Hyperlink

class UserSerializer(serializers.HyperlinkedModelSerializer):
    postings = serializers.HyperlinkedRelatedField(many=True, view_name="posting-detail", read_only=True)

    class Meta:
        model = User
        fields = ("url", "id", "username", "postings")


