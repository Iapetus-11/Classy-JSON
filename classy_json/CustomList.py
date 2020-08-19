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
