import httpx
import pytest
from pytest_httpx import HTTPXMock

from get_json import get_json
from post_json import post_json


def test_get_json(httpx_mock: HTTPXMock) -> None:
    url = 'https://test.ru'
    json_data = {'key': 'value'}
    httpx_mock.add_response(
        method='GET',
        url=url,
        json=json_data,
        status_code=200
    )
    response = get_json(url)
    assert response == json_data


def test_get_json_request_error(httpx_mock: HTTPXMock) -> None:
    url = 'https://test.ru'
    httpx_mock.add_exception(
        method='GET',
        url=url,
        exception=httpx.RequestError('Request Error')
    )
    with pytest.raises(httpx.RequestError):
        get_json(url)


def test_get_json_status_error(httpx_mock: HTTPXMock) -> None:
    url = 'https://test.ru'
    httpx_mock.add_response(
        method='GET',
        url=url,
        status_code=404
    )
    with pytest.raises(httpx.HTTPStatusError) as exception_info:
        get_json(url)
    assert exception_info.value.response.status_code == 404


def test_post_json(httpx_mock: HTTPXMock) -> None:
    url = 'https://test.ru'
    json_data = {'name': 'Alex', 'lastname': 'Tolchin'}
    httpx_mock.add_response(
        method='POST',
        url=url,
        json=json_data,
        status_code=201
    )
    response = post_json(url, json_data)
    assert response == json_data


def test_post_json_request_error(httpx_mock: HTTPXMock) -> None:
    url = 'https://test.ru'
    json_data = {'name': 'Alex', 'lastname': 'Tolchin'}
    httpx_mock.add_exception(
        method='POST',
        url=url,
        exception=httpx.RequestError('Request Error')
    )
    with pytest.raises(httpx.RequestError):
        post_json(url, json_data)


def test_post_json_status_error(httpx_mock: HTTPXMock) -> None:
    url = 'https://test.ru'
    json_data = {'name': 'Alex', 'lastname': 'Tolchin'}
    httpx_mock.add_response(
        method='POST',
        url=url,
        status_code=404
    )
    with pytest.raises(httpx.HTTPStatusError) as exception_info:
        post_json(url, json_data)
    assert exception_info.value.response.status_code == 404
