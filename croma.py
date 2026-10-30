"""A small client for the Croma API: official government data as JSON.

Every endpoint is a POST that answers `{"data": ...}`. Get a key at
https://usecroma.com and export it as CROMA_API_KEY. Docs: https://docs.usecroma.com
"""
import os

import requests

BASE_URL = os.environ.get("CROMA_BASE_URL", "https://api.croma.run")


def has_key() -> bool:
    return bool(os.environ.get("CROMA_API_KEY"))


def call(path: str, **body) -> dict:
    """POST one request and return its `data`."""
    key = os.environ.get("CROMA_API_KEY")
    if not key:
        raise RuntimeError("Set CROMA_API_KEY to query the API (get a key at https://usecroma.com).")
    response = requests.post(
        f"{BASE_URL}{path}",
        json=body,
        headers={"Authorization": f"Bearer {key}"},
        timeout=120,
    )
    response.raise_for_status()
    return response.json()["data"]


def search_all(path: str, max_pages: int = 10, **body) -> list[dict]:
    """Every result of a paginated search, up to `max_pages` pages."""
    results: list[dict] = []
    page = 1
    while page <= max_pages:
        data = call(path, page=page, **body)
        results.extend(data["results"])
        if page >= data.get("total_pages", 1):
            break
        page += 1
    return results
