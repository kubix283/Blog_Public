from blog_app.models import Post
from django.contrib.auth.models import User
from django.test import Client
import datetime
import pytest


@pytest.fixture
def user_client():
    user = User.objects.create_user(username='testuser', password='password')
    client = Client()
    client.login(username='testuser', password='password')
    return client

@pytest.fixture
def post():
    return Post.objects.create(title='test_tytuł', description='jakis opis', date_created=datetime.datetime.now())
    