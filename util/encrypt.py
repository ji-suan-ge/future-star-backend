"""
encrypt

:author: lishanZheng
:date: 2019/12/30
"""
import hashlib


def encrypt(data):
    """
    加密

    :author: lishanZheng
    :date: 2019/12/30
    """
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    res = sha256.hexdigest()
    return res


def compare(before, after):
    """
    比较

    :author: lishanZheng
    :date: 2019/12/30
    """
    before = encrypt(before)
    if before == after:
        return True
    return False
