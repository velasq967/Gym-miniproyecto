"""
Create a dictionary that store the users information
"""

import os
import json

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_PATH, "user.json")


def users_load():
    with open(JSON_PATH, "r") as j:
        data = json.load(j)
        j.close()
    return data

users = users_load()


