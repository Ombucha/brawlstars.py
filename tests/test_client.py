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


# pylint: skip-file

import unittest
from brawlstars.client import Client

# Helper for error simulation

def make_response(status_code):
    class Response:
        def __init__(self):
            self.status_code = status_code
        def json(self):
            return {}
    return Response()

class DummySession:
    def __init__(self):
        self.headers = {}

class TestClient(unittest.TestCase):
    def setUp(self):
        self.token = "testtoken"
        self.client = Client(self.token)

    def test_client_initialization(self):
        self.assertEqual(self.client.session.headers["Authorization"], f"Bearer {self.token}")
        self.assertTrue(hasattr(self.client, "get_player"))
        self.assertTrue(hasattr(self.client, "get_club"))
        self.assertTrue(hasattr(self.client, "get_brawlers"))

    def test_custom_session(self):
        session = DummySession()
        client = Client(self.token, session=session)
        self.assertIs(client.session, session)
        self.assertEqual(client.session.headers["Authorization"], f"Bearer {self.token}")

    def test_on_member_join_returns_decorator(self):
        # Only test decorator returns a callable, do not call the returned function (avoid thread)
        decorator = self.client.on_member_join("#CLUB")
        self.assertTrue(callable(decorator))

    def test_on_member_leave_returns_decorator(self):
        decorator = self.client.on_member_leave("#CLUB")
        self.assertTrue(callable(decorator))

    def test_on_battlelog_update_returns_decorator(self):
        decorator = self.client.on_battlelog_update("#PLAYER")
        self.assertTrue(callable(decorator))

    def test_client_methods_exist(self):
        for method in [
            "get_player_battlelog", "get_player", "get_club_members", "get_club",
            "get_player_rankings", "get_brawler_rankings", "get_club_rankings",
            "get_brawlers", "get_brawler", "get_event_rotation", "on_member_join",
            "on_member_leave", "on_battlelog_update"
        ]:
            self.assertTrue(hasattr(self.client, method), f"Client missing method: {method}")

    def test_missing_token(self):
        with self.assertRaises(TypeError):
            Client()  # Should raise because token is required

    def test_empty_token(self):
        client = Client("")
        self.assertEqual(client.session.headers["Authorization"], "Bearer ")

    def test_forbidden_error(self):
        class ForbiddenSession:
            def __init__(self):
                self.headers = {"Authorization": "Bearer testtoken"}
            def get(self, *args, **kwargs):
                return make_response(403)
        client = Client(self.token, session=ForbiddenSession())
        with self.assertRaises(Exception) as cm:
            client.get_player("#TAG")
        from brawlstars.exceptions import ForbiddenError
        self.assertTrue(isinstance(cm.exception, ForbiddenError))

    def test_resource_not_found_error(self):
        class NotFoundSession:
            def __init__(self):
                self.headers = {"Authorization": "Bearer testtoken"}
            def get(self, *args, **kwargs):
                return make_response(404)
        client = Client(self.token, session=NotFoundSession())
        with self.assertRaises(Exception) as cm:
            client.get_player("#TAG")
        from brawlstars.exceptions import ResourceNotFoundError
        self.assertTrue(isinstance(cm.exception, ResourceNotFoundError))

    def test_rate_limit_error(self):
        class RateLimitSession:
            def __init__(self):
                self.headers = {"Authorization": "Bearer testtoken"}
            def get(self, *args, **kwargs):
                return make_response(429)
        client = Client(self.token, session=RateLimitSession())
        with self.assertRaises(Exception) as cm:
            client.get_player("#TAG")
        from brawlstars.exceptions import RateLimitError
        self.assertTrue(isinstance(cm.exception, RateLimitError))

    def test_unknown_error(self):
        class UnknownSession:
            def __init__(self):
                self.headers = {"Authorization": "Bearer testtoken"}
            def get(self, *args, **kwargs):
                return make_response(500)
        client = Client(self.token, session=UnknownSession())
        with self.assertRaises(Exception) as cm:
            client.get_player("#TAG")
        from brawlstars.exceptions import UnknownError
        self.assertTrue(isinstance(cm.exception, UnknownError))

    def test_maintenance_error(self):
        class MaintenanceSession:
            def __init__(self):
                self.headers = {"Authorization": "Bearer testtoken"}
            def get(self, *args, **kwargs):
                return make_response(503)
        client = Client(self.token, session=MaintenanceSession())
        with self.assertRaises(Exception) as cm:
            client.get_player("#TAG")
        from brawlstars.exceptions import MaintenanceError
        self.assertTrue(isinstance(cm.exception, MaintenanceError))

if __name__ == "__main__":
    unittest.main()
