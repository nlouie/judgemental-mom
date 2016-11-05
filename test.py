import indicoio


def test_me(s, api_key):

    '''
        input s: string of english text 
        input api_key: string api_key for indico
        returns dictionary of emotion values
    '''

    indicoio.config.api_key = api_key
    response = indicoio.emotion(s)
    return response