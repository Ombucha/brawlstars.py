# pylint: skip-file

import os
import sys

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))

on_rtd = os.environ.get("READTHEDOCS") == "True"
project = "brawlstars.py"
copyright = "2025, Omkaar"
author = "Ombucha"
release = "1.2.1"

extensions = ["sphinx.ext.autodoc"]
