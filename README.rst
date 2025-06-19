.. image:: https://raw.githubusercontent.com/Ombucha/brawlstars.py/main/banner.png

.. image:: https://img.shields.io/pypi/v/brawlstars.py
    :target: https://pypi.python.org/pypi/brawlstars.py
    :alt: PyPI version
.. image:: https://static.pepy.tech/personalized-badge/brawlstars.py?period=total&left_text=downloads&left_color=grey&right_color=red
    :target: https://pypi.python.org/pypi/brawlstars.py
    :alt: PyPI downloads
.. image:: https://sloc.xyz/github/Ombucha/brawlstars.py?lower=True
    :target: https://github.com/Ombucha/brawlstars.py/graphs/contributors
    :alt: Lines of code
.. image:: https://img.shields.io/github/repo-size/Ombucha/brawlstars.py?color=yellow
    :target: https://github.com/Ombucha/brawlstars.py
    :alt: Repository size

A modern, and easy-to-use Python wrapper for the official Brawl Stars API.

Features
--------

- Full coverage of the Brawl Stars API
- Simple, Pythonic interface
- Type hints for better editor support
- Built-in rate limit handling
- Pagination and filtering helpers
- Extensive documentation and examples

Requirements
------------

- **Python 3.8 or higher**
- `requests <https://pypi.python.org/pypi/requests>`_

Installation
------------

To install the latest stable version:

.. code-block:: sh

    # Unix / macOS
    python3 -m pip install "brawlstars.py"

    # Windows
    py -m pip install "brawlstars.py"

To install the development version:

.. code-block:: sh

    git clone https://github.com/Ombucha/brawlstars.py
    cd brawlstars.py
    python3 -m pip install -e .

Getting Started
---------------

1. **Get your API token** from https://developer.brawlstars.com/
2. **Install the package** as shown above.
3. **Start coding!**

Quick Example
-------------

.. code-block:: python

    import brawlstars as bs

    client = bs.Client("token")

    # Fetch player info
    player = client.get_player("#9PPUP2CJ")
    print(f"{player.name}: {player.trophies} trophies, {player.team_victories} team victories")

    # Fetch club info and best player
    club = client.get_club(player.club.tag)
    if club:
        members = client.get_club_members(club.tag)
        best_player = max(members, key=lambda m: m.trophies)
        print(f"Best club member: {best_player.name} - {best_player.trophies} 🏆")

    # Top 5 global players
    for player in client.get_player_rankings("global", limit=5):
        print(f"{player.rank}. {player.name} ({player.trophies} 🏆)")

    # Top 10 US players for a specific brawler
    for player in client.get_brawler_rankings("us", 16000043, limit=10):
        print(f"{player.rank}. {player.name} ({player.trophies} 🏆)")

    # Recent battles
    battles = client.get_player_battlelog("#JGCCGY80")
    print("Most recent battle mode:", battles[0].battle.mode)

Advanced Usage
--------------

- **Pagination:** Use `limit` and `after`/`before` parameters for large result sets.
- **Error Handling:** All API errors raise `brawlstars.BrawlStarsException` or subclasses.
- **Rate Limiting:** The client automatically handles rate limits and retries.
- **Custom Session:** Pass your own `requests.Session` for advanced usage.

Links
-----

- `Brawl Stars <https://brawlstars.com/>`_
- `Official API <https://developer.brawlstars.com/>`_
- `Documentation <https://brawlstars.readthedocs.io/>`_
- `Examples <https://github.com/Ombucha/brawlstars.py/tree/main/examples>`_

Contributing
------------

Contributions are welcome! Please see the `contributing guide <https://github.com/Ombucha/brawlstars.py/blob/main/CONTRIBUTING.md>`_.

License
-------

This project is licensed under the MIT License. See the `LICENSE <https://github.com/Ombucha/brawlstars.py/blob/main/LICENSE>`_ file for details.
