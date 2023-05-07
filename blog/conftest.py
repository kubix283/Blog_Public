from blog_app.models import Post
import datetime
import pytest

@pytest.fixture
def post():
    post = Post.objects.create(title='test_tytuł', description='jakis opis', date_created=datetime.datetime.now())
    return post