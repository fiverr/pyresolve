from pyresolve import resolve


my_dictionary = {"outer": {"middle": {"inner": "Balue"}}}
dictionary_with_list = {"list": ["one", "two", list("abcdefghijklmnop")]}
users_list = {"users": [{"name": "Joe"}, {"name": "Jane"}]}


def test_happy_flow():
    assert resolve(my_dictionary, "outer.middle.inner") == "Balue"


def test_missing_prop():
    assert resolve(my_dictionary, "outer.missing.something") is None


def test_fallback_value_false():
    assert resolve(my_dictionary, "outer.missing.something", False) is False


def test_fallback_value_list():
    assert resolve(my_dictionary, "outer.missing.something", []) == []


def test_number_cell():
    assert resolve(dictionary_with_list, "outer.1") is None


def test_dictionary_with_list_number():
    assert resolve(dictionary_with_list, "list.1") is "two"


def test_dictionary_with_list_nested():
    assert resolve(dictionary_with_list, "list.2.012") is "m"


def test_dictionary_with_list_syntax():
    assert resolve(dictionary_with_list, "list[2][1]") is "b"


def test_list_as_target():
    assert resolve(dictionary_with_list["list"], "[2][1]") is "b"


def test_dictionary_with_list_missing():
    assert resolve(dictionary_with_list, "3") is None


def test_dictionary_list_dictionary():
    assert resolve(users_list, "users.1.name") is "Jane"
