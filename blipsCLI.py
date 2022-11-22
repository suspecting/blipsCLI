# blipsCLI
# by venturingfan/suspecting (https://github.com/suspecting)
# with help from the Python Discord

import requests
import argparse

parser = argparse.ArgumentParser(prog = 'blipsCLI', description='Blips from your command line.')
parser.add_argument("-u", "--update", help="Sends update to Blips.")
parser.add_argument("-c", "--credits", help="Credits for blipsCLI")
args = parser.parse_args()

print(args.update) # preview

SigninUrl = 'https://blips.club/signin' # self explanatory
StatusUrl = 'https://blips.club/status/create' # self explanatory


payload = { # used for authentication
    'username': 'Exampleaccount', # Edit this field
    'password': 'Donteventrytologin', # Edit this field
}

session = requests.session() # opens session with said information
resp = session.get(SigninUrl) 
cookie_session = resp.cookies['PHPSESSID']
r = session.post(SigninUrl, data=payload)

payload2 = {
    'session': cookie_session,
    'status': args.update, 
}

r2 = session.post(StatusUrl, data=payload2)