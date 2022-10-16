# pylint: skip-file

import os
import sys

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))

on_rtd = os.environ.get("READTHEDOCS") == "True"
project = "brawlstars.py"
copyright = "2022, Omkaar"
author = "Infiniticity"
release = "1.0.0"

extensions = ["sphinx.ext.autodoc"]
