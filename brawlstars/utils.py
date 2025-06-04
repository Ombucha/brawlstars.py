"""
MIT License

Copyright (c) 2025 Omkaar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import annotations

from typing import Union, TYPE_CHECKING
from urllib.parse import quote

from .exceptions import ForbiddenError, RateLimitError, UnknownError, MaintenanceError, ResourceNotFoundError

if TYPE_CHECKING:
    from .client import Client


def _fetch(url: str, client: Client, params: dict = None) -> Union[list, dict]:
    response = client.session.get(f"https://{quote(url)}", headers = client.session.headers, params = params)
    if response.status_code == 400:
        raise ValueError("the request was malformed, e.g. a required parameter was missing or had an invalid value.")
    if response.status_code == 403:
        raise ForbiddenError("access denied, either because of missing/incorrect credentials or the used API token does not grant access to the requested resource.")
    if response.status_code == 404:
        raise ResourceNotFoundError("resource was not found.")
    if response.status_code == 429:
        raise RateLimitError("request was throttled, because amount of requests was above the threshold defined for the used API token.")
    if response.status_code == 500:
        raise UnknownError("the cause of this error is unknown.")
    if response.status_code == 503:
        raise MaintenanceError("service is temprorarily unavailable because of maintenance.")
    return response.json()


def _difference(list_1: list, list_2: list) -> list:
    result = []
    for element in list_1:
        if element not in list_2:
            result.append(element)
    return result
