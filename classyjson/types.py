"""
Contains the ClassyTypes and the classify function
"""

def classify(val):
    """Used to recursively convert regular containers into ClassyDicts"""

    if isinstance(val, list):
        return ClassyList(val)

    if isinstance(val, dict):
        return ClassyDict(val)

    return val


class ClassyList(list):
    """list subclass required for recursion"""

    def __init__(self, _list=None):
        if _list is None:
            _list = []

        list.__init__(self, map(classify, _list))


class ClassyDict(dict):
    """dict subclass required for dot access"""

    def __init__(self, _dict=None):
        if _dict is None:
            _dict = {}

        dict.__init__(self, {k:classify(v) for (k, v) in _dict.items()})

    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

    def __setattr__(self, name, value):  # ClassyDict.a = 'something'
        return dict.__setitem__(self, name, classify(value))

    def copy(self):
        return classify(dict.copy(self))
