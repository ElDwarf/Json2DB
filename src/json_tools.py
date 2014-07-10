# -*- coding: utf-8 -*-
import json


def load(patch):
    f = open(patch)
    datos = f.read().decode()
    data = json.loads(datos)
    return data
