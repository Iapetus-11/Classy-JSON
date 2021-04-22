"""
Dot-access for Python dictionaries
"""

from json import loads as json_loads
from json import load as json_load
from json import *

from .types import classify, ClassyDict


def loads(*args, **kwargs):
    """Override loads function"""

    return classify(json_loads(*args, **kwargs))


def load(*args, **kwargs):
    """Override load function"""

    return classify(json_load(*args, **kwargs))
