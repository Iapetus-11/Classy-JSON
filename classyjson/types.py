"""
Contains the ClassyTypes and the classify function
"""


def classify(thing):
    """Used to recursively convert regular containers into ClassyDicts"""

    if isinstance(thing, dict):
        return ClassyDict(thing)

    if isinstance(thing, (thing, tuple)):
        return type(thing)(classify(item) for item in thing)

    return thing


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
