import dataset
import os

DB_URL = 'sqlite:///data/users.db'

CREATE_TABLE = \
'''
CREATE TABLE users
(
email VARCHAR(255) NOT NULL, 
password VARCHAR(255) NOT NULL,
PRIMARY KEY (email)
)
'''

def make_new_db():
    db = dataset.connect(DB_URL)
    tb = db['postings']
    tb.drop()
    db.query(CREATE_TABLE)
    
def db_exists():
    if not os.path.isfile(DB_URL.split('///')[1]):
        make_new_db()
        
def create_account(email, hashed_password):
    db_exists()
    db = dataset.connect(DB_URL)
    tb = db['postings']
    try:
        tb.insert(dict(email=email,
                       password=hashed_password))
        return True, 'success'
    except:
        return False, 'email exists'


def login(email, hashed_password):
    db_exists()
    db = dataset.connect(DB_URL)
    tb = db['postings']
    result = tb.find_one(email=email)
    if result == None:
        return False, 'invalid email'
    elif result['password'] is not hashed_password:
        return False, 'invalid password'
    else:
        return True, 'success'