# test.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by nlouie on 11/1/16
# Last updated by nlouie on 11/6/16
# Description:

# ------------------ Imports --------------------- #

import requests

# ------------------ Functions --------------------- #


def test_me(s, api_key):

    '''
        input s: string of english text 
        input api_key: string api_key for indico
        returns dictionary of emotion values
    '''

    headers ={'X-ApiKey':str(api_key)}
    data = {'data': str(s)}
    r = requests.get('https://apiv2.indico.io/emotion/', headers=headers, data=data)
    return r.json()

# eof


import user_database
#
# db = user_database.get_db()
# user_database.create_account('1234', 'bob', 'bob@bon.com')
# all_users = user_database.select_all_users()
# for user in all_users:
#     print(user)