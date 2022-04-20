from rest_framework import serializers
from .models import Band, Album, AlbumReview, AlbumReviewLike

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'name']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'band', 'name', 'image']


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album = serializers.ReadOnlyField(source='album.name')
    album_id = serializers.ReadOnlyField(source='album.id')

    class Meta:
        model = AlbumReview
        fields = ['id', 'album', 'album_id', 'user', 'user_id', 'content', 'score']

class AllAlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    likes = serializers.SerializerMethodField()

    class Meta:
        model = AlbumReview
        fields = ['id', 'album', 'user', 'user_id', 'content', 'score', 'likes']

    def get_likes(self, review):
        return AlbumReviewLike.objects.filter(album_review=review).count()


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = AlbumReviewLike
        fields = ['id', 'user', 'user_id']