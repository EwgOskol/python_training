__author__ = 'tester'

import json

with open("C:/P/config.json") as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res = {}

print(res)
