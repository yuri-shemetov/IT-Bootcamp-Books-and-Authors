from django.urls import path
from rest_framework.routers import DefaultRouter

from authors import views


urlpatterns = [
    path("", views.Authors.as_view(), name="authors"),
    path("<int:pk>/", views.Author.as_view(), name="author"),
    path("create/", views.AuthorCreate.as_view(), name="authors-create"),
    path("update/<int:pk>/", views.AuthorUpdate.as_view(), name="authors-update"),
    path("delete/<int:pk>/", views.AuthorDelete.as_view(), name="authors-delete"),
]
