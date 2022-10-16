brawlstars.py
=============

.. image:: https://img.shields.io/github/license/Infiniticity/brawlstars.py
    :target: https://github.com/Infiniticity/brawlstars.py/blob/main/LICENSE
    :alt: license
.. image:: https://img.shields.io/tokei/lines/github/Infiniticity/brawlstars.py
    :target: https://github.com/Infiniticity/brawlstars.py/graphs/contributors
    :alt: lines of code
.. image:: https://img.shields.io/pypi/v/brawlstars.py
    :target: https://pypi.python.org/pypi/brawlstars.py
    :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/brawlstars.py
    :alt: Python version info


Requirements
------------

This module requires the following modules:

* `requests <https://pypi.python.org/pypi/requests>`_


Installation
------------

**Python 3.8 or higher is required.**

To install the stable version, do the following:

.. code-block:: sh

    # Unix / macOS
    python3 -m pip install "brawlstars.py"

    # Windows
    py -m pip install "brawlstars.py"


To install the development version, do the following:

.. code-block:: sh

    $ git clone https://github.com/Infiniticity/brawlstars.py


Quick Example
-------------

.. code-block:: py

    import brawlstars as bs

    client = bs.Client("token")

    player = client.get_player("#9PPUP2CJ")
    print(player.trophies)
    print(player.team_victories)

    club = client.get_club(player.club.tag)
    if club is not None:
        members = client.get_club_members(club.tag)

        best_player = max(members, key = lambda member: member.trophies)
        print(best_player.name, f"- best_player.trophies 🏆")

    player_rankings = client.get_player_rankings("global", limit = 5)
    for player in player_ranking:
        print(f"{player.rank}. {player.name}")

    brawler_rankings = client.get_brawler_rankings(region = "us", limit = 10, brawler = "edgar")
    for player in brawler_rankings:
        print(f"{player.rank}. {player.name}")

    battles = client.get_battle_logs("UL0GCC8")
    print(battles[0].battle.mode)

More examples can be viewed in the `examples <https://github.com/Infiniticity/brawlstars.py/tree/main/examples>`_ folder.


Links
-----

- `Brawl Stars <https://brawlstars.com/>`_
- `Documentation <https://brawlstars.readthedocs.io/>`_
