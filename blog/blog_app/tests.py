import pytest
from .models import Post


@pytest.mark.django_db
def test_post_model(post):
    assert len(Post.objects.all()) == 1
    assert Post.objects.get(title='test_tytuł') == post
