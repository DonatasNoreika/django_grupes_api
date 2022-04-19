from rest_framework import serializers
from .models import Band, Album, AlbumReview

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'name']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'band', 'name']


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album = serializers.ReadOnlyField(source='album.name')
    album_id = serializers.ReadOnlyField(source='album.id')

    class Meta:
        model = AlbumReview
        fields = ['id', 'album', 'album_id', 'user', 'user_id', 'content', 'score']