from user_database import *

oa = 'oauth1'
n = 'Corey'
e = '09volt@gmail.com'

tests = ['create_account(oa, n, e)', \
         'refresh_account(oa, n, n)', \
         'add_app_token(oa, "whooa")', \
         'is_app_token_valid(oa)']

for test in tests:
    print('>>> ' + test)
    print(eval(test))