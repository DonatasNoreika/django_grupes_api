from django.contrib import admin
from django.urls import path, include
from .views import BandList, BandDetail, AlbumList, AlbumDetail, BandAlbumList, AlbumReviewList

urlpatterns = [
    path('bands', BandList.as_view()),
    path('bands/<int:pk>', BandDetail.as_view()),
    path('albums', AlbumList.as_view()),
    path('albums/<int:pk>', AlbumDetail.as_view()),
    path('bands/<int:pk>/albums', BandAlbumList.as_view()),
    path('albums/<int:pk>/reviews', AlbumReviewList.as_view()),
]