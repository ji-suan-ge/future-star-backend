"""
dictionary util

:author: gexuewen
:date: 2020/01/04
"""


def remove_key(target, key):
    """
    remove the key in dictionary

    :author: gexuewen
    :date: 2020/01/04
    """
    result = dict(target)
    del result[key]
    return result
