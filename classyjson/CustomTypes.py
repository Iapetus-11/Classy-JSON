
def nice(val):
    if isinstance(val, list):
        return CustomList(val)

    if isinstance(val, dict):
        return CustomDict(val)

    return val


class CustomList(list):
    def __init__(self, _list):
        list.__init__(self, map(nice, _list))


class CustomDict(dict):
    def __init__(self, _dict):
        dict.__init__(self, {k: nice(v) for k, v, in _dict.items()})

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
