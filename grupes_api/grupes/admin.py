from django.contrib import admin

# Register your models here.

from .models import (Band,
                     Album,
                     AlbumReview,
                     AlbumReviewComment,
                     AlbumReviewLike)

admin.site.register(Band)
admin.site.register(Album)
admin.site.register(AlbumReview)
admin.site.register(AlbumReviewComment)
admin.site.register(AlbumReviewLike)
