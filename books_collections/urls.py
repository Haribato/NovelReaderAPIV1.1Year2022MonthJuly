from rest_framework import routers
from django.urls import path, include

from .views import *

router = routers.SimpleRouter()

router.register(r'typeBookmarks', TypeBookmarksViewSet)
router.register(r'bookmarks', BookmarksViewSet)

urlpatterns = [

    path('', include(router.urls))
]


