"""
Dot-access for Python dictionaries and more
"""

__version__ = '3.0.1'

from json import loads as json_loads
from json import load as json_load
from json import *

from .types import classify, ClassyDict

def loads(*args, **kwargs):
    """Override loads function"""

    _data = json_loads(*args, **kwargs)
    return classify(_data)

def load(*args, **kwargs):
    """Override load function"""

    _data = json_load(*args, **kwargs)
    return classify(_data)
