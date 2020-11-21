"""
Contains the ClassyTypes and the classify function
"""


def classify(thing):
    """Used to recursively convert regular containers into ClassyDicts"""

    if isinstance(thing, dict):  # Convert dict to dot-accessible ClassyDict
        return ClassyDict(thing)

    # This adds support for iterables which are subclasses or instances of lists and tuples
    if isinstance(thing, (list, tuple)):
        return type(thing)(classify(item) for item in thing)

    return thing


class ClassyDict(dict):
    """dict subclass required for dot access"""

    def __init__(self, _dict=None):
        if _dict is None:  # Allow for creating a new ClassyDict via CLassyDict()
            _dict = {}

        dict.__init__(self, {k:classify(v) for (k, v) in _dict.items()})

    # Override the attribute methods to add dot access
    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

    def __setattr__(self, name, value):  # Add dot-access ClassyDict.a = 'something'
        return dict.__setitem__(self, name, classify(value))

    def copy(self):  # Actually is a deep copy unlike the default shallow .copy()
        return classify(dict.copy(self))
