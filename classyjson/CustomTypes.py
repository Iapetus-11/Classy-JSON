
def objectify(data, key):
    if isinstance(data, list):
        data[key] = CustomList(data[key])
    elif isinstance(data, dict):
        data[key] = CustomDict(data[key])

    return data[key]


class CustomList(list):
    def __init__(self, _list):
        for i, val in enumerate(_list):
            objectify(_list, i)

        list.__init__(self, _list)


class CustomDict(dict):
    def __init__(self, _dict):
        for key in list(_dict):
            objectify(_dict, key)

        dict.__init__(self, _dict)

    def __getattr__(self, name):  # CustomDict.a
        return dict.__getitem__(self, name)

    def __setattr__(self, name, value):  # CustomDict.a = 'something'
        if isinstance(value, list):
            return dict.__setitem__(self, name, CustomList(value))
        elif isinstance(value, dict):
            return dict.__setitem__(self, name, CustomDict(value))

        return dict.__setitem__(self, name, value)

    def __delattr__(self, name):  # del CustomDict.a
        dict.__delitem__(self, name)
