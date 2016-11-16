# analyze.py


def analyze(result):
    """

    :param result: The Facebook oAuth result
    :return:
    """
    # https://developers.facebook.com/docs/graph-api/reference/

    # fields

    name = result.user.name
    oauth_id = result.user.id           # save this in db
    about = ""
    artists_likes = []
    relationship_status = ""


    if result.user.credentials:
        if result.provider.name == 'fb':
            # get all the dirt

            url = 'https://graph.facebook.com/{0}?fields=about%2Creligion%2Cmusic.limit(10)%2Crelationship_status' \
                  '%2Cfeed.limit(10)%2Cemail%2Cfriends%2Clikes.limit(10)%2Cpolitical%birthday'.format(oauth_id)

            response = result.provider.access(url)
            if response.status == 200:
                if 'error' in response.data:
                    raise Exception("Invalid response: " + response.status)
                data = response.data
                print(data)

                # extract data

                if 'about' in data:
                    about = data['about']
                if 'religion' in data:
                    pass
                if 'music' in data:
                    for artist in data['music']['data']:
                        artists_likes += [artist['name']]
                if 'relationship_status' in data:
                    relationship_status = data['relationship_status']
                if 'feed' in data:
                    pass
                if 'email' in data:
                    pass
                if 'friends' in data:
                    pass
                if 'likes' in data:
                    pass
                if 'political' in data:
                    pass





    else:
        raise Exception("Invalid credentials")



