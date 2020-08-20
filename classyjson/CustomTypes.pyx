
class CustomList(list):
    def __init__(self, _list):
        cdef int i
        for i, val in enumerate(_list):
            if isinstance(val, list):
                _list[i] = CustomList(val)
            elif isinstance(val, dict):
                _list[i] = CustomDict(val)

        list.__init__(self, _list)


class CustomDict(dict):
    def __init__(self, _dict):
        cdef str c
        for key in list(_dict):
            if isinstance(_dict[key], list):
                _dict[key] = CustomList(_dict[key])
            elif isinstance(_dict[key], dict):
                _dict[key] = CustomDict(_dict[key])

        dict.__init__(self, _dict)

    def __getattr__(self, name):  # CustomDict.a
        return dict.__getitem__(self, name)

    def __setattr__(self, name, value):  # CustomDict.a = 'something'
        return dict.__setitem__(self, name, value)

    def __delattr__(self, name):  # del CustomDict.a
        popped = dict.__getitem__(key)
        dict.__delitem__(self, key)
        return popped
