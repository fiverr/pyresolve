# -*- coding: utf-8 -*-

def resolve(obj, path, fallback=None):
    """
    Retrieve nested properties safely
    Example: resolve(
      {"out":{"middle":{"in":"Balue"}}},
      "out.middle.in"
    ) → "Balue"
    :param obj: Dictionary
    :param path: cot notation representation of dictionary
    :param fallback: what to return for unresolved items (default:None)
    :rtype: any
    """
    for name in path.split("."):
        if name in obj:
            obj = obj[name]
        else:
            return fallback
    return obj
