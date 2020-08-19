class CustomList(list):
    def __init__(self, _list):
        for i, val in enumerate(_list):
            if isinstance(val, list):
                _list[i] = CustomList(val)
            elif isinstance(val, dict):
                _list[i] = CustomDict(val)

        list.__init__(self, _list)
