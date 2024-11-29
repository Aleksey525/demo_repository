import random
from unittest.mock import patch


def my_random_function():
    return random.randint(1, 100)


def test_my_random_function():
    with patch('random.randint', return_value=55) as mock_randint:
        result = my_random_function()
        assert result == 55
        mock_randint.assert_called_once_with(1, 100)
