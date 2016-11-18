# connect.py
def extract_facebook(result):
    """

    :param result: The Facebook oAuth result
    :return output: dictionary of data
    """
    # https://developers.facebook.com/docs/graph-api/reference/

    # fields
    name = result.user.name             # save this in db
    oauth_id = result.user.id           # save this in db (note this is unique to our app key)

    output = {'name': name,
              'email': "",
              'oauth_id': oauth_id,
              'about': "",
              'religion': "",
              'artist_likes': [],
              'relationship_status': "",
              'posts_data': {},
              'likes_data': {},
              'political': "",
              'num_friends': "",
              'birthday': "",
              'gender': ""
              }

    if result.user.credentials:
        if result.provider.name == 'fb':

            # get all the dirt

            url = 'https://graph.facebook.com/{0}?fields=about%2Cgender%2Creligion%2Cmusic.limit(10)%2C' \
                  'relationship_status%2Cposts.limit(100)%2Cemail%2Cfriends%2Clikes.limit(10)%2Cpolitical%2Cbirthday'
            url = url.format(oauth_id)

            response = result.provider.access(url)
            if response.status == 200:
                if 'error' in response.data:
                    raise Exception("Invalid response: " + response.status)
                data = response.data

                # extract data and add to output dictionary
                # important to perform input validation!

                if 'about' in data:
                    output['about'] = data.get('about')
                if 'gender' in data:
                    output['gender'] = data.get('gender')
                if 'religion' in data:
                    output['religion'] = data.get('religion')
                if 'music' in data:
                    for artist in data.get('music').get('data'):
                        artists = []
                        artists += [artist.get('name')]
                        output['artists_likes'] = artists
                if 'relationship_status' in data:
                    output['relationship_status'] = data.get('relationship_status')
                if 'feed' in data:
                    output['posts_data'] = data.get('posts').get('data')
                    output['posts_paging'] = data.get('posts').get('paging')           # paging:{previous:"",next:""}
                if 'email' in data:
                    output['email'] = data.get('email')
                if 'friends' in data:
                    output['num_friends'] = data.get('friends').get('summary').get('total_count')
                if 'likes' in data:
                    output['likes_data'] = data.get('likes').get('data')
                    # paging:{cursors:{before:"", after:""}, next:""}
                    output['likes_paging'] = data.get('likes').get('paging')
                if 'political' in data:
                    output['political'] = data.get('political')
                if 'birthday' in data:
                    output['birthday'] = data.get('birthday')
        print(output)
        return output
    else:
        raise Exception("Invalid credentials")



