from django.conf.urls.static import static
from rest_framework import routers
from django.urls import path, include

from books.views import *

router = routers.SimpleRouter()

router.register(r'books', BooksViewSet, basename='booksViewSet')
router.register(r'language', LanguageViewSet, basename='languageViewSet')
router.register(r'status', StatusViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'source', SourceViewSet)

urlpatterns = [
    # path('img/<slug:sl>/', img),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




