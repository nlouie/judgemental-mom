# config.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by corey on 11/5/16
# Last updated by corey on 11/17/16
# Description:

# ------------------ Imports --------------------- #

from json import load


# ------------------ Functions --------------------- #

def load_auth_json():
    data = load(open('auth.json', 'r'))
    return data
