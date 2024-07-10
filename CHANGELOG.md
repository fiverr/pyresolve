# Changelog

## 1.2.0

Accept list notation (square brackets) as well as dot notation

```py
dictionary_with_list = {"list": ["One", "Two", "Three"]}
resolve(my_dictionary, "list[1]") # Two
```

## 1.1.0

### Support index
You can now pull specific items out of a list

```py
dictionary_with_list = {"list": ["One", "Two", "Three"]}
resolve(my_dictionary, "list.1") # Two
```
