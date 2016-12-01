# database.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by corey on 11/5/16
# Last updated by nlouie on 12/01/16
# Description: Creates a database

# ------------------ Imports --------------------- #

import dataset

# ------------------ Params ---------------------- #

DB_URL = 'sqlite:///data/app.db'

TABLE_NAME_USERS = 'users'

TABLE_SCHEMA = \
    '''
    CREATE TABLE IF NOT EXISTS ''' + TABLE_NAME_USERS + '''
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fb_name VARCHAR(255) NOT NULL,
        fb_email VARCHAR(255) NOT NULL UNIQUE,
        fb_oauth_token VARCHAR(255) NOT NULL UNIQUE,
        fb_app_token VARCHAR(255),
        num_uses INTEGER NOT NULL DEFAULT 0
    );
    '''


# ------------------ Helpers --------------------- #


def get_db():
    db = dataset.connect(DB_URL)
    db.query(TABLE_SCHEMA)
    return db


# ------------------ Publics --------------------- #

def create_account(fb_oauth_token, fb_name, fb_email):
    """
    Insert account
    :param fb_oauth_token:
    :param fb_name:
    :param fb_email:
    :return:
    """
    db = get_db()
    tb = db[TABLE_NAME_USERS]
    try:
        tb.insert(dict(fb_name=fb_name,
                       fb_email=fb_email,
                       fb_oauth_token=fb_oauth_token))
        return True
    except Exception as e:
        return False

        # table.update(dict(name='John Doe', age=47), ['name'])


def refresh_account(fb_oauth_token, fb_name, fb_email):
    """
    Update account
    :param fb_oauth_token: str
    :param fb_name: str
    :param fb_email: str
    :return:
    """
    db = get_db()
    tb = db[TABLE_NAME_USERS]
    try:
        tb.update(dict(fb_name=fb_name,
                       fb_email=fb_email,
                       fb_oauth_token=fb_oauth_token), ['fb_oauth_token'])
        return True
    except Exception as e:
        return False


def add_app_token(fb_oauth_token, fb_app_token):
    """
    Add the oauth token.
    :param fb_oauth_token: str
    :param fb_app_token: str
    :return:
    """
    db = get_db()
    tb = db[TABLE_NAME_USERS]
    try:
        tb.update(dict(fb_app_token=fb_app_token,
                       fb_oauth_token=fb_oauth_token), ['fb_oauth_token'])
        return True
    except Exception as e:
        return False


def select_all_users():
    """
    SELECT *
    FROM users;
    :return:
    """
    return dataset.connect(DB_URL)[TABLE_NAME_USERS].all()


def increment_num_uses(fb_oauth_token):
    """
    UPDATE users
    SET num_uses = num_uses + 1
    WHERE oauth_id = fb_oauth_token
    :param fb_oauth_token:
    :return:
    """
    db = get_db()
    tb = db[TABLE_NAME_USERS]
    user = tb.find_one(fb_oauth_token=fb_oauth_token)
    user_num_uses = user['num_uses']
    try:
        tb.update(dict(fb_oauth_token=fb_oauth_token,
                       num_uses=user_num_uses + 1), ['fb_oauth_token'])
        return True
    except Exception as e:
        return False
