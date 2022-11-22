# blipsCLI
# by venturingfan/suspecting (https://github.com/suspecting)
# with help from the Python Discord

import requests
import argparse
import feedparser

parser = argparse.ArgumentParser(prog = 'blipsCLI', description='Blips from your command line.')
parser.add_argument("-u", "--update", help="Sends update to Blips.")
parser.add_argument('-d','--direct', nargs='+', help='Sends Direct Message to Blips user.')
parser.add_argument('-f', '--feed', action='store_true', help='Shows last 10 statuses.')
parser.add_argument('-s', '--star', help='Star/Favorite a status by status number.')
args = parser.parse_args()

print(args) # preview

SigninUrl = 'https://blips.club/signin'
StatusUrl = 'https://blips.club/status/create'
DirectUrl = 'https://blips.club/direct_messages/create'
FavoriteUrl = 'https://blips.club/favorites/create'


AuthPayload = { # used for authentication
    'username': 'testing', # Edit this field
    'password': 'helloworld', # Edit this field
}

session = requests.session()
resp = session.get(SigninUrl) 
cookie_session = resp.cookies['PHPSESSID']
AuthResponse = session.post(SigninUrl, data=AuthPayload)


if args.update:
    UpdatePayload = {
        'session': cookie_session,
        'status': args.update, 
    }
    
    UpdateResponse = session.post(StatusUrl, data=UpdatePayload)

if args.direct:
    DirectPayload = {
        'session': cookie_session,
        'status': args.direct[1],
        'recipient': args.direct[0]
    }
    
    DirectResponse = session.post(DirectUrl, data=DirectPayload)

if args.feed:
    Feed = feedparser.parse("https://blips.club/" + AuthPayload['username'] + "/with_friends.rss")
    for i in range(10):
        PostId = Feed.entries[i].link.replace('https://blips.club/testing/statuses/', '')
        print(Feed.entries[i].title + " / Status #" + PostId)

if args.star:
    FavoritePayload = {
        'session': cookie_session,
        'id': args.star,
    }
    
    FavoriteResponse = session.post(FavoriteUrl, data=FavoritePayload)
