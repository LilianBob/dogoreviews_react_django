from rest_framework import routers
from drbooks.api import BookViewSet, ReviewViewSet

router= routers.DefaultRouter()
router.register('api/books', BookViewSet, 'books')
router.register('api/reviews', ReviewViewSet, 'reviews')

urlpatterns= router.urls