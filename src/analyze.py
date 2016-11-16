# analyze.py


def analyze(result):
    """

    :param result: The Facebook oAuth result
    :return:
    """
    # https://developers.facebook.com/docs/graph-api/reference/

    # fields
    name = result.user.name             # save this in db
    oauth_id = result.user.id           # save this in db (note this is unique to our app key)
    email = ""                          # save this in db

    # -- Never store personal information below --- #
    about = ""
    religion = ""
    artists_likes = []
    relationship_status = ""
    feed_data = {}
    likes_data = {}
    political = ""
    num_friends = -1
    birthday = ""
    gender = ""


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

                # extract data

                if 'about' in data:
                    about = data['about']
                if 'gender' in data:
                    gender = data['gender']
                if 'religion' in data:
                    pass
                if 'music' in data:
                    for artist in data['music']['data']:
                        artists_likes += [artist['name']]
                if 'relationship_status' in data:
                    relationship_status = data['relationship_status']
                if 'feed' in data:
                    feed_data = data['posts']['data']
                    feed_paging = data['posts']['paging']                   # paging:{previous:"",next:""}
                if 'email' in data:
                    email = data['email']
                if 'friends' in data:
                    num_friends = data['friends']['data']['summary']['total_count']
                if 'likes' in data:
                    likes_data = data['likes']['data']
                    likes_paging = data['likes']['paging']            # paging:{cursors:{before:"", after:""}, next:""}
                if 'political' in data:
                    political = data['political']
                if 'birthday' in data:
                    birthday = data['birthday']


    else:
        raise Exception("Invalid credentials")



