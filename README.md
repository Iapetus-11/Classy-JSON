# Classy-JSON ![PYPI Downloads](https://img.shields.io/pypi/dw/classy-json?color=64b594) ![PYPI Version](https://img.shields.io/pypi/v/classy-json.svg) [![Views](https://api.ghprofile.me/view?username=iapetus-11.classy-json&color=51B780&label=Views&style=flat)](https://github.com/Villager-Dev/Villager-Bot)
### `dict.key` (Dot access) for Python dictionaries

## How do I use Classy-JSON?
* Classy-JSON can be used nearly identically to the regular built-in json module! [json module docs](https://docs.python.org/3/library/json.html)
* The only differences are that you can now access dictionaries via `dict.key` as well as `dict['key']`, and that the .copy() method is now a deep copy.
* Using `dict.key` is about 2-2.5x slower \[in some cases\] than using `dict['key']`, however, using `dict['key']` is just as fast as in normal Python dictionaries. For most use cases, this difference is negligible.
* What seperates Classy-JSON and its custom data structures from other alternatives? Classy-JSON is both better in its speed and package size, other similiar packages have unecessary code and just aren't as fast as Classy-JSON

## Example Usage
```py
import classyjson as cj

# load data from a json file
with open('tests/test_large.json', 'r') as f:
  data = cj.load(f)

# turn a regular dictionary into a ClassyDict
my_dict = {'a': 'b'}
my_classy_dict = cj.classify(my_dict)
# or
my_classy_dict = cj.ClassyDict(my_dict)

# make a new ClassyDict
new_classy_dict = cj.ClassyDict()
```

## Setup / Install
### Using pip:
```
python3 -m pip install classy-json
```
### Manually:
* Clone the repository
```
git clone https://github.com/Iapetus-11/Classy-JSON.git
```
* cd into the directory
```
cd Classy-JSON
```
* Run setup.py
```
python3 setup.py build install
```

## Contribution
* Fork the repository
* Make any changes
* Submit a pull request
