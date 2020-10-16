
def classify(val):
    if isinstance(val, list):
        return NiceList(val)

    if isinstance(val, dict):
        return ClassyDict(val)

    return val


class NiceList(list):
    def __init__(self, _list):
        list.__init__(self, map(classify, _list))


class ClassyDict(dict):
    def __init__(self, _dict):
        dict.__init__(self, {k:classify(v) for (k, v) in _dict.items()})

    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

    def __setattr__(self, name, value):  # ClassyDict.a = 'something'
        return dict.__setitem__(self, name, classify(value))
