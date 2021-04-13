from ..classyjson import *

def test_creation():
    d = ClassyDict()
    d = ClassyDict({})
    d = ClassyDict({"a": "b", "c": [1, 2, 3]})
    d = classify({"a": "b", "c": [1, 2, 3, {"a": "b"}]})

    assert isinstance(d["c"][3], ClassyDict)

def test_usage():
    d = ClassyDict({"a": "b", "c": [1, 2, 3]})

    d.a
    d.c[1]
