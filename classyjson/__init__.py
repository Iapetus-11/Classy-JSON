"""
Dot-access for Python dictionaries and more
"""

from json import loads as json_loads
from json import load as json_load
from json import *

from .types import *

def loads(*args, **kwargs):
    _data = json_loads(*args, **kwargs)
    return classify(_data)

def load(*args, **kwargs):
    _data = json_load(*args, **kwargs)
    return classify(_data)
