# Classy-Json ![PYPI Downloads](https://img.shields.io/pypi/dw/classy-json?color=64b594) ![PYPI Version](https://img.shields.io/pypi/v/classy-json.svg)
### An attempt at recreating the way json works in JavaScript, but in the Python programming language.

## How do I use classy-json?
* All functions from the built in json module are supported! [json module docs](https://docs.python.org/3/library/json.html)
* The only difference is that you can now access dictionaries via `dict.key` as well as `dict['key']`
* Note: using `dict.key` is about 2-2.5x slower \[in some cases\] than using `dict['key']`, however, using `dict['key']` is just as fast as in normal Python dictionaries.
* You can also use `classyjson.classify(Union[dict, list, actually anything])` to turn a preexisting dictionary or list into a ClassyDict or ClassyList object

## Setup / Install
### Using pip:
```
python3 -m pip install classy-json
```
### Manually:
* Clone the repository
```
git clone https://github.com/Iapetus-11/classy-json.git
```
* cd into the directory
```
cd classy-json
```
* Run setup.py
```
python3 setup.py build install
```

## Contribution
* Fork the repository
* Make any changes
* Submit a pull request
