from .CustomTypes import CustomList, CustomDict
import json

def objectify(data, threaded):
    if isinstance(data, list):
        return CustomList(data, threaded)
    elif isinstance(data, dict):
        return CustomDict(data, threaded)
    else:
        return data

def loads(data, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, threaded=False):
    _data = json.loads(
        data, cls=cls, object_hook=object_hook, parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook
    )

    return objectify(_data, threaded)

def load(io, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, threaded=False):
    _data = json.load(io, cls=cls, object_hook=object_hook, parse_float=parse_float, parse_int=parse_int,
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook)

    return objectify(_data, threaded)

def dumps(data, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None,
          separators=None, default=None, sort_keys=False):
    return json.dumps(data, skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular,
                      allow_nan=allow_nan, cls=cls, indent=indent, separators=separators, default=default,
                      sort_keys=sort_keys
    )

def dump(data, io, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None,
         separators=None, default=None, sort_keys=False):
    return json.dump(data, io, skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular,
                     allow_nan=allow_nan, cls=cls, indent=indent, separators=separators, default=default,
                     sort_keys=sort_keys
    )
