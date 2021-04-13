from classyjson import *


def test_creation():
    d = ClassyDict()
    d = ClassyDict({})
    d = ClassyDict({"a": "b", "c": [1, 2, 3]})
    d = classify({"a": "b", "c": [1, 2, 3, {"a": "b"}]})

    assert isinstance(d["c"][3], ClassyDict)


def test_usage():
    d = ClassyDict({"a": "b", "c": [1, 2, 3]})

    assert "a" in d

    assert d["a"] == "b"
    assert d.a == "b"
    assert d["c"][0] == 1
    assert d.c[0] == 1


    d.e = "abcdefhijklmonpqrstuv"

    assert "e" in d

    assert d["e"] == "abcdefhijklmonpqrstuv"
    assert d.e == "abcdefhijklmonpqrstuv"

    del d["e"]

    assert "e" not in d
