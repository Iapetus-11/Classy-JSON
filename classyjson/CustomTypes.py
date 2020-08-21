
def nice(val):
    if isinstance(val, list):
        return CustomList(val)
    elif isinstance(val, dict):
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

    def __getattr__(self, name):  # CustomDict.a
        return dict.__getitem__(self, name)

    def __setattr__(self, name, value):  # CustomDict.a = 'something'
        return dict.__setitem__(self, name, nice(value))

    def __delattr__(self, name):  # del CustomDict.a
        dict.__delitem__(self, name)
