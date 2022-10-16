brawlstars.py
==========

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

Make sure you have the latest version of Python installed, or if you prefer, a Python version of 3.8 or greater.

If you have have any other issues feel free to search for duplicates and then create a new issue on GitHub with as much detail as possible. Include the output in your terminal, your OS details and Python version.


Client
-----

.. autoclass:: brawlstars.Client
    :members:


Models
----------

.. autoclass:: brawlstars.Battlelog
    :members:

.. autoclass:: brawlstars.BrawlStarsObject
    :members:

.. autoclass:: brawlstars.BrawlerList
    :members:

.. autoclass:: brawlstars.ClubMemberList
    :members:

.. autoclass:: brawlstars.ClubRanking
    :members:

.. autoclass:: brawlstars.EventList
    :members:

.. autoclass:: brawlstars.Player
    :members:

.. autoclass:: brawlstars.PlayerRanking
    :members:
    
.. autoclass:: brawlstars.PowerPlaySeasonList
    :members:


Exceptions
---------------

.. autoclass:: brawlstars.BrawlStarsException
    :members:

.. autoclass:: brawlstars.ForbiddenError
    :members:

.. autoclass:: brawlstars.MaintenanceError
    :members:

.. autoclass:: brawlstars.RateLimitError
    :members:

.. autoclass:: brawlstars.UncallableError
    :members:

.. autoclass:: brawlstars.UnknownError
    :members:
