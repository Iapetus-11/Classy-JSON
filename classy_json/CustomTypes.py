class CustomList(list):
    def __init__(self, _list):
        for i, val in enumerate(_list):
            if isinstance(val, list):
                _list[i] = CustomList(val)
            elif isinstance(val, dict):
                _list[i] = CustomDict(val)

        list.__init__(self, _list)

class CustomDict(dict):
    def __init__(self, _dict):
        dict.__init__(self, _dict)

        for key in list(_dict):
            if isinstance(_dict[key], list):
                self.__dict__[key] = CustomList(_dict[key])
            elif isinstance(_dict[key], dict):
                self.__dict__[key] = CustomDict(_dict[key])
            else:
                self.__dict__[key] = _dict[key]

    def __setitem__(self, key, value):
        dict[key] = value
        self.__dict__[key] = value

    def __delitem__(self, key):
        val = dict[key]

        dict.pop(key)
        self.__dict__.pop(key)

        return val
