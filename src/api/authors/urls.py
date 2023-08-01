from rest_framework.routers import DefaultRouter

from authors import views


router = DefaultRouter()
router.register(r"authors-list", views.AuthorViewSet, basename="authors-list")

urlpatterns = router.urls
