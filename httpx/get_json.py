import httpx


def get_json(url: str) -> dict | list | None:
    try:
        response = httpx.get(url)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as exc:
        print(f'An error occurred while requesting {exc.request.url!r}.')
        raise
    except httpx.HTTPStatusError as exc:
        print(f'Error response {exc.response.status_code} while requesting {exc.request.url!r}.')
        raise exc
