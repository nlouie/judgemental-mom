# test.py
# Judgemental Mom
# CS411 A2 Group 8 Project
# Created by nlouie on 11/1/16
# Last updated by nlouie on 11/6/16
# Description:

# ------------------ Imports --------------------- #
import indicoio

# ------------------ Functions --------------------- #


def test_me(s, api_key):

    '''
        input s: string of english text 
        input api_key: string api_key for indico
        returns dictionary of emotion values
    '''

    indicoio.config.api_key = api_key
    response = indicoio.emotion(s)
    return response

# eof
