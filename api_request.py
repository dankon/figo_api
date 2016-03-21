#-*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Module for provide some API action
"""
import re
import webbrowser
import base64
import json

import requests


# Demo Client ID: CaESKmC8MAhNpDe5rvmWnSkRE_7pkkVIIgMwclgzGcQY
demo_client_id = 'CaESKmC8MAhNpDe5rvmWnSkRE_7pkkVIIgMwclgzGcQY'
# Demo Client Secret: STdzfv0GXtEj_bwYn7AgCVszN1kKq5BdgEIKOM_fzybQ
demo_client_secret = 'STdzfv0GXtEj_bwYn7AgCVszN1kKq5BdgEIKOM_fzybQ'
# Demo Access Token: ASHWLIkouP2O6_bgA2wWReRhletgWKHYjLqDaqb0LFfamim9RjexTo22ujRIP_cjLiRiSyQXyt2kM1eXU2XLFZQ0Hro15HikJQT_eNeT_9XQ

# Demo User Login: demo@figo.me
# Demo User Password: demo1234


MAIN_URL = 'https://api.figo.me'

AUTH_URL = ("https://api.figo.me/auth/code?response_type=code&"
            "client_id=CaESKmC8MAhNpDe5rvmWnSkRE_7pkkVIIgMwclgzGcQY&"
            "scope=accounts%3Dro+balance%3Dro+transactions%3Dro&state=xqD6gjWygsBlF0uB")

webbrowser.open(AUTH_URL)
            
AUTH_STRING = raw_input('Provide code:\n')
            
code = re.search(r'(?<=code=)[A-Za-z0-9-_]+', AUTH_STRING).group(0)

print "#######################################\n"
print code
print "#######################################\n"

POST_AUTH_TOKEN_URL = ("https://api.figo.me/auth/token")
AUTH_TOKEN_PARAMS = {'grant_type' : 'authorization_code',
                     'code' : code}
auth_headers = {'Authorization': "Basic %s" % base64.b64encode(demo_client_id + ":" + demo_client_secret),
                'Accept': 'application/json', 
                'Content-Type': 'application/x-www-form-urlencoded'} 
                     
auth_token_req = requests.post(POST_AUTH_TOKEN_URL, data=AUTH_TOKEN_PARAMS, headers=auth_headers)

print auth_token_req.text

req_response = json.loads(auth_token_req.text)

print req_response['access_token']

access_headers = {'Authorization': "%s %s" % (req_response['token_type'], req_response['access_token']), 
                  'Accept': 'application/json', 
                  'Content-Type': 'application/json'}

with open('auth_token.js', 'w') as tok_file:
    tok_file.write('var headers = ' + json.dumps(access_headers) + ';')
"""\
user_req = requests.get('%s/rest/user' % MAIN_URL, headers=access_headers)
print user_req.text

#GET /rest/accounts/<account_id>
accounts_req = requests.get('%s/rest/accounts' % MAIN_URL, headers=access_headers)
print accounts_req.text

#GET /rest/accounts/<account_id>/balance

#GET /rest/banks/<bank_id>

#GET /rest/accounts/<account_id>/transactions/<transaction_id>
#GET /rest/transactions/<transaction_id>
"""



