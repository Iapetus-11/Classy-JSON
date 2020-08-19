from .CustomTypes import CustomList, CustomDict
import json
from typing import Union

def loads(data: str) -> Union[CustomList, CustomDict]:
    _data = json.loads(data)

    if isinstance(_data, list):
        return CustomList(_data)
    elif isinstance(_data, dict):
        return CustomDict(_data)
    else:
        return data

def load(io) -> Union[CustomList, CustomDict]:
    return loads(io.read())
