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

    def __setitem__(self, key, value):  # CustomDict['a'] = 'something'
        dict.__setitem__(key, value)
        self.__dict__[key] = value

    def __setattr__(self, name, value):  # CustomDict.a = 'something'
        dict.__setitem__(name, value)
        self.__dict__[name] = value

    def __delitem__(self, key):  # CustomDict.pop('a')
        dict.__delitem__(key)
        return self.__dict__.pop(key)

    def __delattr__(self, name):  # del CustomDict.a
        dict.__delitem__(name)
        return self.__dict__.pop(key)
