import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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


def test_time():
    od = {"a": "b", "c": "d", "e": [1, 2, 3, 4, 5]}
    cd = ClassyDict(od.copy())

    od_t = time.time()
    for _ in range(100000):
        od["a"]
    od_t = time.time() - od_t

    cd_t = time.time()
    for _ in range(100000):
        cd.a
    cd_t = time.time() - cd_t

    print(f"ACCESS: CJ: {cd_t} | D: {od_t} | diff: {cd_t - od_t}")
