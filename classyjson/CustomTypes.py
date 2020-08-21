
def nice(val):
    if isinstance(val, list):
        return CustomList(val)

    if isinstance(val, dict):
        return CustomDict(val)

    return val


class CustomList(list):
    def __init__(self, _list):
        map(nice, _list)
        list.__init__(self, _list)


class CustomDict(dict):
    def __init__(self, _dict):
        for key in list(_dict):
            if isinstance(_dict[key], list):
                _dict[key] = CustomList(_dict[key])
            elif isinstance(_dict[key], dict):
                _dict[key] = CustomDict(_dict[key])

        dict.__init__(self, _dict)

    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

    def __setattr__(self, name, value):  # CustomDict.a = 'something'
        return dict.__setitem__(self, name, nice(value))
