from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from authors import models, forms


class Authors(ListView):
    model = models.Author
    template_name = "authors/authors.html"


class Author(DetailView):
    model = models.Author
    template_name = "authors/author.html"


class AuthorCreate(CreateView):
    model = models.Author
    form_class = forms.AuthorsForm
    template_name = "authors/author_create.html"


class AuthorUpdate(UpdateView):
    model = models.Author
    form_class = forms.AuthorsForm
    template_name = "authors/author_update.html"


class AuthorDelete(DeleteView):
    model = models.Author
    success_url = reverse_lazy("authors")
    template_name = "authors/author_delete.html"
