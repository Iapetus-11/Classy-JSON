"""
Contains the ClassyTypes and the classify function
"""


def classify(thing):
    """Used to recursively convert regular containers into ClassyDicts"""

    # convert dict to ClassyDict
    if isinstance(thing, dict):
        return ClassyDict(thing)

    # attempt to convert items of a list to ClassyDicts
    if isinstance(thing, list):
        return [classify(item) for item in thing]

    # attempt to convert items of a tuple to ClassyDicts
    if isinstance(thing, tuple):
        return tuple(classify(item) for item in thing)

    return thing


class ClassyDict(dict):
    """dict subclass required for dot access"""

    def __init__(self, _dict=None):
        if _dict is None:  # allow for creating a new ClassyDict via CLassyDict()
            dict.__init__(self)
        else:
            dict.__init__(self, {k: classify(v) for (k, v) in _dict.items()})

    # override the attribute methods to add dot access
    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

    def __setattr__(self, name, value):  # add dot-access ClassyDict.a = 'something'
        return dict.__setitem__(self, name, classify(value))

    def copy(self):  # actually is a deep copy unlike the default shallow .copy()
        return classify(dict.copy(self))
