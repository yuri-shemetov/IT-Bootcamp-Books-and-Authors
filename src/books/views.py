from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from books import models, forms


class Books(ListView):
    model = models.Book
    template_name = "books/books.html"
    ordering = "name"
    paginate_by = 9


class Book(DetailView):
    model = models.Book
    template_name = "books/book.html"


class BookCreate(CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = "books/book_create.html"


class BookUpdate(UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = "books/book_update.html"


class BookDelete(DeleteView):
    model = models.Book
    success_url = reverse_lazy("books")
    template_name = "books/book_delete.html"
