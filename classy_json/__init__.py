import json
from typing import Union

class CustomList(list):
    def __init__(self, _list):
        list.__init__(self, _list)

        for i, val in enumerate(_list):
            self.__dict__[f'_{i}'] = val

class CustomDict(dict):
    def __init__(self, _dict):
        dict.__init__(self, _dict)

    for key in list(_dict):
        self.__dict__[key] = _dict[key]
