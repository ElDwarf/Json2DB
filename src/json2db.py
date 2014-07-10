# -*- coding: utf-8 -*-
from settings import MODELS
from json_tools import load
from models import models


def initializer(variables_array=None):
    models_tmp = {}
    for model in MODELS:
        tmp_name = model['name']
        models_tmp[tmp_name] = models(
            load(model['patch'])
        )
        fkey = []
        for x in model['foreignkey']:
            fkey.append(x)
        for key in fkey:
            for x in models_tmp[tmp_name].table:
                x[key['related_name']] = models_tmp[key['model_to']].get(
                    key['col_to'], x[key['col_from']]
                )
            del x[key['col_from']]
        if variables_array is not None:
            variables_array[tmp_name] = models_tmp[tmp_name]
            return variables_array
    return models_tmp
