
def nice(val):
    if isinstance(val, list):
        return NiceList(val)

    if isinstance(val, dict):
        return NiceDict(val)

    return val


class NiceList(list):
    def __init__(self, _list):
        map(nice, _list)
        list.__init__(self, _list)


class NiceDict(dict):
    def __init__(self, _dict):
        for key in list(_dict):
            if isinstance(_dict[key], list):
                _dict[key] = NiceList(_dict[key])
            elif isinstance(_dict[key], dict):
                _dict[key] = NiceDict(_dict[key])

        dict.__init__(self, _dict)

    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

    def __setattr__(self, name, value):  # NiceDict.a = 'something'
        return dict.__setitem__(self, name, nice(value))
