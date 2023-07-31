import pytest
from authors.models import Author


@pytest.fixture
def author(db) -> Author:
    return Author.objects.create(name="Dummy")


def test_author_creation(author: Author) -> None:
    assert author.id == 1
    assert author.name == "Dummy"


def test_authors_list(client, author) -> None:
    response = client.get("/authors/")
    assert response.status_code == 200
    assert response.context["object_list"].count() == 1
    assert response.context["object_list"].first() == author


def test_author_delete(client, author) -> None:
    response = client.get(f"/authors/delete/{author.id}/")
    assert response.status_code == 200
    assert response.context["object"] == author
    response = client.post(f"/authors/delete/{author.id}/")
    assert response.context == None
