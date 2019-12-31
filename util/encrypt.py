import hashlib


def encrypt(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    res = sha256.hexdigest()
    return res


def compare(before, after):
    before = encrypt(before)
    if before == after:
        return True
    return False
