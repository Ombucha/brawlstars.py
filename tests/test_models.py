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
from brawlstars.models import (
    BrawlStarsObject, Battlelog, Player, ClubMemberList, PlayerRanking, ClubRanking, EventList
)
from datetime import datetime

class TestModels(unittest.TestCase):
    def test_brawlstarsobject_flat_and_nested(self):
        data = {"fooBar": 1, "nested": {"barBaz": 2}, "lst": [{"bazQux": 3}]}
        obj = BrawlStarsObject(data)
        self.assertEqual(obj.foo_bar, 1)
        self.assertIsInstance(obj.nested, BrawlStarsObject)
        self.assertEqual(obj.nested.bar_baz, 2)
        self.assertIsInstance(obj.lst[0], BrawlStarsObject)
        self.assertEqual(obj.lst[0].baz_qux, 3)

    def test_brawlstarsobject_eq(self):
        a = BrawlStarsObject({"foo": 1, "bar": 2})
        b = BrawlStarsObject({"foo": 1, "bar": 2})
        c = BrawlStarsObject({"foo": 1, "bar": 3})
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_battlelog_len_and_datetime(self):
        dt = "20250101T120000.000Z"
        data = {"items": [{"battleTime": dt}]}
        log = Battlelog(data)
        self.assertEqual(len(log), 1)
        self.assertIsInstance(log[0].battle_time, datetime)

    def test_player_team_victories(self):
        data = {"tag": "#TAG", "3vs3Victories": 10}
        player = Player(data)
        self.assertEqual(player.team_victories, 10)

    def test_clubmemberlist_name_color(self):
        data = {"items": [{"nameColor": "0xFFFFFF"}]}
        members = ClubMemberList(data)
        member = members[0]
        self.assertEqual(member.name_color, hex(int("0xFFFFFF", 16)))

    def test_playerranking_name_color(self):
        data = {"items": [{"nameColor": "0xFFFFFF"}]}
        ranking = PlayerRanking(data)
        player = ranking[0]
        self.assertEqual(player.name_color, hex(int("0xFFFFFF", 16)))

    def test_clubranking_index(self):
        data = {"items": [{"foo": 1}]}
        ranking = ClubRanking(data)
        club = ranking[0]
        self.assertIsInstance(club, BrawlStarsObject)

    def test_eventlist_datetime(self):
        dt1 = "20250101T120000.000Z"
        dt2 = "20250102T120000.000Z"
        data = [{"startTime": dt1, "endTime": dt2}]
        events = EventList(data)
        event = events[0]
        self.assertIsInstance(event.start_time, datetime)
        self.assertIsInstance(event.end_time, datetime)

if __name__ == "__main__":
    unittest.main()
