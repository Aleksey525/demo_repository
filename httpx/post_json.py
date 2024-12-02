import httpx


def post_json(url: str, data: dict) -> dict | list | None:
    try:
        response = httpx.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}.")
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
        raise exc