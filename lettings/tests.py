import pytest
from django.urls import reverse

from .models import Letting, Address


@pytest.fixture
def address():
    address = Address.objects.create(number="1234", street="teamwork", city="Saint-PriPri",
                                     state="california", zip_code="90210", country_iso_code="222")
    return address


@pytest.fixture
def letting(address):
    letting = Letting.objects.create(title="Fixture", address=address)
    print(letting.title, letting.address)
    return letting


class TestLettingsView:
    @pytest.mark.django_db
    def test_letting_index(self, client, letting):
        response = client.get(reverse('lettings_index'))

        assert response.status_code == 200
        assert b'<title>Lettings</title>' in response.content

    @pytest.mark.django_db
    def test_letting_id(self, client, letting):
        response = client.get(reverse('letting', args=[letting.id]))

        assert response.status_code == 200
        assert b'<title>Fixture</title>' in response.content
