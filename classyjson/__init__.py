"""
Dot-access for Python dictionaries and more
"""

from json import loads as json_loads
from json import load as json_load
from json import *

from .types import *

def loads(data, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None):
    _data = json_loads(
        data, cls=cls, object_hook=object_hook, parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook
    )

    return classify(_data)

def load(io, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None):
    _data = json_load(io, cls=cls, object_hook=object_hook, parse_float=parse_float, parse_int=parse_int,
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook)

    return classify(_data)
