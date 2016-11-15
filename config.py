# config.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by corey on 11/5/16
# Last updated by nlouie on 11/6/16
# Description:

# ------------------ Imports --------------------- #

import json

# ------------------ Functions --------------------- #


def load_auth_json():
    data = json.load(open('auth.json', 'r'))
    return data


