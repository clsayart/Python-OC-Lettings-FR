import pytest
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


@pytest.fixture
def profile():
    user = User.objects.create_user(username='Testuser', first_name='Test', last_name='User',
                                    email='testuser@gmail.com')
    profile = Profile.objects.create(user=user, favorite_city='Paris')
    print(user.username, profile.user)
    return profile


class TestProfileView:
    @pytest.mark.django_db
    def test_profile_index(self, client, profile):
        response = client.get(reverse('profiles_index'))

        assert response.status_code == 200
        assert b'<title>Profiles</title>' in response.content

    @pytest.mark.django_db
    def test_profile_id(self, client, profile):
        response = client.get(reverse('profile', args=[profile.user.username]))

        assert response.status_code == 200
        assert b'<title>Testuser</title>' in response.content
