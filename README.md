# pyresolve [![](https://img.shields.io/pypi/v/pyresolve?style=flat-square)](https://pypi.org/project/pyresolve/) [![](https://img.shields.io/static/v1?label=github&message=pyresolve&labelColor=black&color=3572a5&style=flat-square&logo=github)](https://github.com/fiverr/pyresolve)

Resolve dot notation from dictionary

```py
from pyresolve import resolve

my_dictionary = {"out":{"middle":{"in":"Balue"}}}

resolve(my_dictionary, "out.middle.in") # "Balue"
```

Does not break for missing properties
```py
resolve(my_dictionary, "outer.missing.something") # None
```

Can specify a different default value
```py
resolve(my_dictionary, "outer.missing.something", False) # False
```

Install

```bash
pip install pyresolve
```
