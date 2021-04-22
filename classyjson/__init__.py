"""
Dot-access for Python dictionaries
"""

__version__ = "3.1.0"

from json import loads as json_loads
from json import load as json_load
from json import *

import pyximport

pyximport.install(language_level=3)

from .types import classify, ClassyDict


def loads(*args, **kwargs):
    """Override loads function"""

    return classify(json_loads(*args, **kwargs))


def load(*args, **kwargs):
    """Override load function"""

    return classify(json_load(*args, **kwargs))
