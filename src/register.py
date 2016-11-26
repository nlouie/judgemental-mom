# register.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by nlouie on 11/12/16
# Last updated by nlouie on 11/18/16
# Description: Handles user registration to database

from database import *


def db_user(user_data):
    """
    :param user_data:
    :return:
    """
    user_exists = not create_account(user_data['oauth_id'],
                                     user_data['name'],
                                     user_data['email'])

    if user_exists:
        # in case email or name changed
        refresh_account(user_data['oauth_id'],
                        user_data['name'],
                        user_data['email'])

    # user doesn't exist
    else:
        # do whatever you want here
        # user is already created once you get here
        pass

