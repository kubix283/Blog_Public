import pytest
from .models import Post
import datetime
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

@pytest.mark.django_db
def test_post_model(post):
    assert len(Post.objects.all()) == 1
    assert Post.objects.filter(title='test_tytuł').exists


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

@pytest.mark.django_db
def test_post_list_view(user_client):
    response = user_client.get(reverse('post_list'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'post_list.html')

@pytest.mark.django_db
def test_post_detail_view(user_client, post):
    response = user_client.get(reverse('post_detail', args=[post.pk]))
    assert response.status_code == 200
    assertTemplateUsed(response, 'post_detail.html')
    assert response.context['post'] == post 


@pytest.mark.django_db
def test_post_create_view(user_client):
    data = {'title': 'title', 'description': 'description', 'date_created': datetime.datetime.now()}
    response = user_client.post(reverse('post_create'), data=data)
    assert response.status_code == 302
    assert Post.objects.filter(title='title').exists()


@pytest.mark.django_db
def test_post_update_view(user_client, post):
    data = {'title': 'new title', 'description': 'new description', 'date_created': datetime.datetime.now()}
    response = user_client.post(reverse('post_update', args=[post.pk]), data=data)
    assert response.status_code == 302
    post.refresh_from_db()
    assert Post.objects.filter(title='new title').exists()


@pytest.mark.django_db
def test_post_delete_view(user_client, post):
    response = user_client.post(reverse('post_delete', args=[post.pk]))
    assert response.status_code == 302
    assert not Post.objects.filter(pk=post.pk).exists()
