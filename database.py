# database.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by corey on 11/5/16
# Last updated by corey on 11/17/16
# Description:

# ------------------ Imports --------------------- #

import dataset
from config import load_auth_json

PARAMS = load_auth_json()

def get_db():
    db = dataset.connect(PARAMS['database']['url'])
    db.query(PARAMS['database']['table_schema'])
    return db

def create_account(fb_name, fb_email, fb_oauth_token):
    db = get_db()
    tb = db[PARAMS['database']['table']]
    try:
        tb.insert(dict(fb_name=fb_name,
                       fb_email=fb_email,
                       fb_oauth_token=fb_oauth_token))
        return True
    except Exception as e:
        #print(e)
        return False