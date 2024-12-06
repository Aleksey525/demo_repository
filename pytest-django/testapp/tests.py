from django.contrib.auth.models import User

import pytest


@pytest.mark.django_db
def test_create_user() -> None:
    name = 'test_user'
    email = 'test@test.com'
    password = 'test_password'
    user = User.objects.create_user(name, email, password)
    user.save()

    assert User.objects.filter(username=name).exists()
    assert User.objects.get(username=name).email == email
    assert User.objects.get(username=name).check_password(password) is True


@pytest.mark.django_db
def test_check_user_exclusion() -> None:
    with pytest.raises(User.DoesNotExist, match=r'User matching query does not exist'):
        User.objects.get(username='no_exists_user')