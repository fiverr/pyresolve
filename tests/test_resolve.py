from pyresolve import resolve


my_dictionary = {"outer": {"middle": {"inner": "Balue"}}}


def test_happy_flow():
    assert resolve(my_dictionary, "outer.middle.inner") == "Balue"


def test_missing_prop():
    assert resolve(my_dictionary, "outer.missing.something") is None


def test_fallback_value_false():
    assert resolve(my_dictionary, "outer.missing.something", False) is False


def test_fallback_value_list():
    assert resolve(my_dictionary, "outer.missing.something", []) == []
