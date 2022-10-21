"""
MIT License

Copyright (c) 2022 Omkaar

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


class BrawlStarsException(Exception):

    """
    Base exception class for this library.
    """

    pass


class ForbiddenError(BrawlStarsException):

    """
    An exception that is raised when access is denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.
    """

    pass


class RateLimitError(BrawlStarsException):

    """
    An exception that is raised when the amount of requests was above the threshold defined for the used API token.
    """

    pass


class UnknownError(BrawlStarsException):

    """
    An exception that is raised when an unknown error occurs while handling the request.
    """

    pass


class MaintenanceError(BrawlStarsException):

    """
    An exception that is raised when the service is temporarily unavailable because of maintenance.
    """

    pass


class ResourceNotFoundError(BrawlStarsException):

    """
    An exception that is raised when the resource is not found.
    """

    pass


class UncallableError(BrawlStarsException):

    """
    An exception that is raised when a function is not callable.
    """

    pass
