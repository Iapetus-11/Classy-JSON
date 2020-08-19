import json
from typing import Union

class CustomList(list):
    def __init__(self, _list):
        list.__init__(self, _list)

        for i, val in enumerate(_list):
            if isinstance(val, list):
                self.__dict__[f'_{i}'] = CustomList(val)
            elif isinstance(val, dict):
                self.__dict__[f'_{i}'] = CustomDict(val)
            else:
                self.__dict__[f'_{i}'] = val

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
