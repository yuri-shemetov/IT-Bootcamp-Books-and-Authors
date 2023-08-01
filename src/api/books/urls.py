from rest_framework.routers import DefaultRouter

from books import views


router = DefaultRouter()
router.register(r"books-list", views.BookViewSet, basename="books-list")

urlpatterns = router.urls
