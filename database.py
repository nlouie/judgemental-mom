# database.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by corey on 11/5/16
# Last updated by corey on 11/17/16
# Description:

# ------------------ Imports --------------------- #

import dataset

# ------------------ Params ---------------------- #

DB_URL = 'sqlite:///data/app.db'

TABLE_NAME = 'users'

TABLE_SCHEMA = \
    '''
    CREATE TABLE IF NOT EXISTS ''' + TABLE_NAME + '''
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fb_name VARCHAR(255) NOT NULL,
        fb_email VARCHAR(255) NOT NULL UNIQUE,
        fb_oauth_token VARCHAR(255) NOT NULL UNIQUE,
        fb_app_token VARCHAR(255)
    )
    '''

# ------------------ Helpers --------------------- #


def get_db():
    db = dataset.connect(DB_URL)
    db.query(TABLE_SCHEMA)
    return db

# ------------------ Publics --------------------- #


def create_account(fb_oauth_token, fb_name, fb_email):
    db = get_db()
    tb = db[TABLE_NAME]
    try:
        tb.insert(dict(fb_name=fb_name,
                       fb_email=fb_email,
                       fb_oauth_token=fb_oauth_token))
        return True
    except Exception as e:
        return False
    
    # table.update(dict(name='John Doe', age=47), ['name'])


def refresh_account(fb_oauth_token, fb_name, fb_email):
    db = get_db()
    tb = db[TABLE_NAME]
    try:
        tb.update(dict(fb_name=fb_name,
                       fb_email=fb_email,
                       fb_oauth_token=fb_oauth_token), ['fb_oauth_token'])
        return True
    except Exception as e:
        return False


def add_app_token(fb_oauth_token, fb_app_token):
    db = get_db()
    tb = db[TABLE_NAME]
    try:
        tb.update(dict(fb_app_token=fb_app_token,
                       fb_oauth_token=fb_oauth_token), ['fb_oauth_token'])
        return True
    except Exception as e:
        return False

# # depreciate this.
#
# def is_app_token_valid(fb_oauth_token):
#     db = get_db()
#     tb = db[TABLE_NAME]
#     try:
#         return bool(tb.find_one(fb_oauth_token=fb_oauth_token)['fb_app_token_fresh'])
#     except Exception as e:
#         print(e)
