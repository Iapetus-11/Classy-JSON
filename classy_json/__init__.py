from .CustomList import CustomList

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
