import pytest
from authors.models import Author
from books.models import Book


@pytest.fixture
def author(db) -> Author:
    return Author.objects.create(name="Dummy")


@pytest.fixture
def book(db, author: Author) -> Book:
    book = Book.objects.create(
        picture="photo.jpg",
        name="Dummy",
        price=10,
        year=2023,
        pages=100,
        quantity=3,
        avtive=True,
    )
    book.author.set([author])
    return book


def test_author_creation(author: Author) -> None:
    assert author.id == 1
    assert author.name == "Dummy"


def test_book_creation(book: Book) -> None:
    assert book.id == 1
    assert book.picture == "photo.jpg"
    assert book.name == "Dummy"
    assert book.price == 10
    assert book.year == 2023
    assert book.pages == 100
    assert book.quantity == 3
    assert book.avtive == True


def test_books_list(client, book: Book) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.context["object_list"].count() == 1
    assert response.context["object_list"].first() == book


def test_author_delete(client, book: Book) -> None:
    response = client.get(f"/delete/{book.id}/")
    assert response.status_code == 200
    assert response.context["object"] == book
    response = client.post(f"/delete/{book.id}/")
    assert response.context == None
