# analyze.py

def analyze(user_data):

    results = {} # output

    # get all the message strings
    messages = []
    for post in user_data['posts_data']:
        if 'message' in post:
            messages += post['message']
    print(messages)

    return results
