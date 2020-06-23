from pyresolve import resolve


my_dictionary = {"outer": {"middle": {"inner": "Balue"}}}


def test_happy_flow():
    assert resolve(my_dictionary, "outer.middle.inner") == "Balue"


def test_missing_prop():
    assert resolve(my_dictionary, "outer.missing.something") is None


def test_default_fallback():
    assert resolve(my_dictionary, "outer.missing.something", False) is False
