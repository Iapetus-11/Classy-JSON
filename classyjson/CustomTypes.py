
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

    def __getattr__(self, name):  # CustomDict.a
        return dict.__getitem__(self, name)

    def __setattr__(self, name, value):  # CustomDict.a = 'something'
        return dict.__setitem__(self, name, nice(value))

    def __delattr__(self, name):  # del CustomDict.a
        dict.__delitem__(self, name)
