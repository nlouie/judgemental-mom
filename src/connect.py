# connect.py
def connect_facebook(result):
    """

    :param result: The Facebook oAuth result
    :return output: dictionary of data
    """
    # https://developers.facebook.com/docs/graph-api/reference/

    # fields
    name = result.user.name             # save this in db
    oauth_id = result.user.id           # save this in db (note this is unique to our app key)
    email = ""                          # save this in db

    # -- Never store personal information below in db --- #
    # about = ""
    # religion = ""
    # artists_likes = []
    # relationship_status = ""
    # feed_data = {}
    # likes_data = {}
    # political = ""
    # num_friends = -1
    # birthday = ""
    # gender = ""

    output = {'name': name,
              'oauth_id': oauth_id,
              'about': "",
              'religion': "",
              'artist_likes': "",
              'relationship_status': "",
              'feed_data': {},
              'likes_data': {},
              'political': "",
              'num_friends': -1,
              'birthday': "",
              'gender': ""
              }

    # -- Never store personal information above in db -- #

    if result.user.credentials:
        if result.provider.name == 'fb':

            # get all the dirt

            url = 'https://graph.facebook.com/{0}?fields=about%2%gender2CCreligion%2Cmusic.limit(10)%2C' \
                  'relationship_status%2Cfeed.limit(10)%2Cemail%2Cfriends%2Clikes.limit(10)%2Cpolitical%birthday'\
                .format(oauth_id)

            response = result.provider.access(url)
            if response.status == 200:
                if 'error' in response.data:
                    raise Exception("Invalid response: " + response.status)
                data = response.data
                print(data)

                # extract data and add to output dictionary
                # important to perform input validation!

                if 'about' in data:
                    about = data['about']
                if 'gender' in data:
                    gender = data['gender']
                if 'religion' in data:
                    pass
                if 'music' in data:
                    for artist in data['music']['data']:
                        output['artists_likes'] += [artist['name']]
                if 'relationship_status' in data:
                    output['relationship_status'] = data['relationship_status']
                if 'feed' in data:
                    output['feed_data'] = data['posts']['data']
                    feed_paging = data['posts']['paging']                   # paging:{previous:"",next:""}
                if 'email' in data:
                    output['email'] = data['email']
                if 'friends' in data:
                    output['num_friends'] = data['friends']['data']['summary']['total_count']
                if 'likes' in data:
                    output['likes_data'] = data['likes']['data']
                    output['likes_paging'] = data['likes']['paging']  # paging:{cursors:{before:"", after:""}, next:""}
                if 'political' in data:
                    output['political'] = data['political']
                if 'birthday' in data:
                    output['birthday'] = data['birthday']

            # pass data to analysis


        return output
    else:
        raise Exception("Invalid credentials")



