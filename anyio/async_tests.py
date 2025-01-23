from httpx import HTTPStatusError, RequestError
import pytest
from pytest_httpx import HTTPXMock
from pytest_mock import MockerFixture

from async_requests import main, send_request


@pytest.mark.anyio
async def test_send_requests(httpx_mock: HTTPXMock) -> None:
    url = 'https://api.test'
    mock_response = {'ip': '127.0.0.1'}
    httpx_mock.add_response(
        method='GET',
        url=url,
        json=mock_response,
        status_code=200
    )
    result = await send_request(url)
    assert result == mock_response


@pytest.mark.anyio
async def test_send_requests_http_error(httpx_mock: HTTPXMock) -> None:
    url = 'https://api.test'
    httpx_mock.add_response(
        method='GET',
        url=url,
        status_code=404
    )
    with pytest.raises(HTTPStatusError):
        await send_request(url)


@pytest.mark.anyio
async def test_send_requests_request_error(httpx_mock: HTTPXMock) -> None:
    url = 'https://api.test'
    httpx_mock.add_exception(
        method='GET',
        url=url,
        exception=RequestError('error')
    )
    with pytest.raises(RequestError):
        await send_request(url)


@pytest.mark.anyio
async def test_main(mocker: MockerFixture) -> None:
    mock_send_request = mocker.AsyncMock()
    mock_send_request.side_effect = [
        {"test_1": "127.0.0.1"},
        {"test_2": '127.0.0.2'},
        {"test_3": '127.0.0.3'},
    ]
    mocker.patch('async_requests.send_request', mock_send_request)
    await main()
    assert mock_send_request.call_count == 3
