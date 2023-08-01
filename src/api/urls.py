from django.urls import path, include

from authors import views


urlpatterns = [
    path("authors/", include("api.authors.urls")),
    path("books/", include("api.books.urls")),
]
