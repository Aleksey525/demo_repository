from django.contrib.auth.models import User

import pytest


@pytest.mark.django_db
class TestUser:

    def test_create_user(self) -> None:
        user = User.objects.create_user('test_user', 'test@test.com', 'test_password')
        user.save()

        assert User.objects.filter(username='test_user').exists()
        assert User.objects.get(username='test_user').email == 'test@test.com'
        assert User.objects.get(username='test_user').check_password('test_password') is True

    def test_check_user_exclusion(self) -> None:
        with pytest.raises(User.DoesNotExist, match=r'User matching query does not exist'):
            User.objects.get(username='no_exists_user')
