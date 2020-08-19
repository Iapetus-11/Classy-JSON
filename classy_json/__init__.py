from .CustomList import CustomList
from .CustomDict import CustomDict
import json

def loads(data: str):
    _data = json.loads(data)

    if isinstance(_data, list):
        return CustomList(_data)
    elif isinstance(_data, dict):
        return CustomDict(_data)
    else:
        return data

def load(io):
    return loads(io.read())
