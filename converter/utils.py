#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from inspect import getsource
from hashlib import md5


def checkInputs(a, b):
    if a == None and b == None:
        raise ValueError("Un des deux paramètres doit être renseigné")
    elif a != None and b != None:
        raise ValueError("Seulement un des deux paramètres doit être renseigné")
    else:
        pass


def funcChecksum(func):
    """Renvoie le hash md5 d'un fonction"""
    code = getsource(func)
    code = "".join([line.strip() for line in code.split("\n") if line != ''])
    hash = md5(code.encode())
    return hash.hexdigest()
