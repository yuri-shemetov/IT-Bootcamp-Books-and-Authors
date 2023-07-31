from django.urls import path
from books import views

urlpatterns = [
    path("", views.Books.as_view(), name="books"),
    path("<int:pk>/", views.Book.as_view(), name="book"),
    path("create/", views.BookCreate.as_view(), name="book-create"),
    path("update/<int:pk>/", views.BookUpdate.as_view(), name="book-update"),
    path("delete/<int:pk>/", views.BookDelete.as_view(), name="book-delete"),
]
