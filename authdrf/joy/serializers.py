from django.contrib.auth.models import User, Group
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import serializers, generics, permissions
from .models import Poem


class PoemSerializer(serializers.ModelSerializer):
    # read-only to make the api set the author by default
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Poem
        fields = ['id', 'title', 'content', 'author']

    def create(self, validated_data):
        # when creating a new poem, set the author to the current user
        validated_data['author'] = self.context['request'].user
        return super(PoemSerializer, self).create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )


