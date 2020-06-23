# pyresolve

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
