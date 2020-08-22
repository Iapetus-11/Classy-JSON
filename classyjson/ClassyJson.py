from .CustomTypes import NiceList, NiceDict
from json import *

def objectify(data):
    if isinstance(data, list):
        return NiceList(data)
    elif isinstance(data, dict):
        return NiceDict(data)
    else:
        return data

def loads(data, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None):
    _data = json.loads(
        data, cls=cls, object_hook=object_hook, parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook
    )

    return objectify(_data,)

def load(io, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None):
    _data = json.load(io, cls=cls, object_hook=object_hook, parse_float=parse_float, parse_int=parse_int,
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook)

    return objectify(_data)
