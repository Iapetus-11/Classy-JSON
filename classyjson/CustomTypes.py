
def nice(val):
    if isinstance(val, list):
        return NiceList(val)

    if isinstance(val, dict):
        return NiceDict(val)

    return val


class NiceList(list):
    def __init__(self, _list: list = []):
        list.__init__(self, [*map(nice, _list)])


class NiceDict(dict):
    def __init__(self, _dict: dict = {}):
        dict.__init__(self, {k:nice(v) for (k, v) in _dict.items()})

    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

    def __setattr__(self, name, value):  # NiceDict.a = 'something'
        return dict.__setitem__(self, name, nice(value))
