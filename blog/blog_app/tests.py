import pytest
from .models import Post
import datetime


@pytest.mark.django_db
def test_post_model(post):
    assert len(Post.objects.all()) == 1
    assert Post.objects.get(title='test_tytuł') == post


@pytest.mark.django_db
def test_post_add():
    post1 = Post.objects.create(title='test_tytuł', description='jakis opis', date_created=datetime.datetime.now())
    assert post1.id is not None
    assert post1.title == 'test_tytuł'
    assert post1.description == 'jakis opis'


@pytest.mark.django_db
def test_update_post():
    post1 = Post.objects.create(title='test_tytuł', description='jakis opis', date_created=(2020, 1, 1))
    post1.title = 'tytul test'
    post1.description = 'inny opis'
    post1.save()

    updated_post = Post.objects.get(id=post1.id)
    assert updated_post.title == 'tytul test'
    assert updated_post.description == 'inny opis'


@pytest.mark.django_db
def test_post_delete():
    post = Post.objects.create(title='test_tytuł', description='jakis opis', date_created=(2020, 1, 1))
    post.save()
    assert len(Post.objects.all()) == 1
    post.delete()
    assert len(Post.objects.all()) == 0