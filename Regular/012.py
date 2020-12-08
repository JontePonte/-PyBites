'''
Bite 12. Write a user validation function ☆
Create a function that takes a username and checks for a valid user:

The username is in USERS,
the user is not expired, and
the user has the ADMIN role.
If those 3 conditions are met return SECRET.

If one of the conditions is not True raise an exception you define yourself: UserDoesNotExist, UserAccessExpired and UserNoPermission respectively. 
'''


from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here

def get_secret_token(username):
    if not username in USERS:
        raise UserDoesNotExist
    return SECRET


print(get_secret_token(pybites))