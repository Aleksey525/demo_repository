from typing import Any, Dict

from httpx import AsyncClient, HTTPStatusError, RequestError
from anyio import create_task_group, run


async def send_request(url: str) -> Dict[str: Any]:
    async with AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            print(f'{url} - {response.json()}')
            return response.json()
        except HTTPStatusError as error:
            print(f'{url} - ошибка: {error.response.status_code}')
            raise error
        except RequestError as error:
            print(f'{url} - ошибка: {str(error)}')
            raise


async def main() -> None:

    urls = [
        'https://official-joke-api.appspot.com/random_joke',
        'https://official-joke-api.appspot.com/random_joke',
        'https://official-joke-api.appspot.com/random_joke',
    ]
    async with create_task_group() as tg:
        for url in urls:
            tg.start_soon(send_request, url)

run(main)
