"""
letter util

:author: lishanZheng
:date: 2020/01/08
"""
from xpinyin import Pinyin


def get_letter(name):
    """
    get first letter

    :author: lishanZheng
    :date: 2020/01/08
    """
    pinyin = Pinyin()
    if name == '':
        return 'Z'
    letter = pinyin.get_initials(name, u'')[0]
    return letter


def cmp(temp1, temp2):
    """
    compare first letter

    :author: lishanZheng
    :date: 2020/01/08
    """
    if get_letter(temp1.name[0]) < get_letter(temp2.name[0]):
        return -1
    return 1
