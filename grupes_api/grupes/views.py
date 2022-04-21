from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from .models import Band, Album, AlbumReview, AlbumReviewLike
from .serializers import (BandSerializer,
                          AlbumSerializer,
                          AlbumReviewSerializer,
                          AllAlbumReviewSerializer,
                          AlbumReviewLikeSerializer,
                          UserSerializer)
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

class BandList(generics.ListAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class BandList(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        # post = Band.objects.filter(pk=kwargs['pk'])
        if self.request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Trinti gali tik administratorius!')

    def put(self, request, *args, **kwargs):
        # post = Band.objects.filter(pk=kwargs['pk'])
        if self.request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Redaguoti gali tik administratorius!')



class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def delete(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Trinti gali tik administratorius!')

    def put(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('Redaguoti gali tik administratorius!')


class BandAlbumList(generics.ListCreateAPIView):
    # queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        band = Band.objects.get(pk=self.kwargs['pk'])
        return Album.objects.filter(band=band)


class AlbumReviewList(generics.ListCreateAPIView):
    # queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album = Album.objects.get(pk=self.kwargs['pk'])
        return AlbumReview.objects.filter(album=album)

    def perform_create(self, serializer):
        album = Album.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album=album)


class AllAlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AllAlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewLikeCreate(generics.ListCreateAPIView):
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # user = self.request.user
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        return AlbumReviewLike.objects.filter(album_review=album_review)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('Jūs jau palikote patiktuką šiai apžvalgai!')
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_review=album_review)

    # def delete(self, request, *args, **kwargs):
    #     album_review = AlbumReview.objects.get(pk=self.kwargs['pk'], user=self.request.user)
    #     if album_review:
    #         self.get_queryset().delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         raise ValidationError('Jūs nepalikote patiktuko po šiuo pranešimu!')


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )