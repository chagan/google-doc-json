#!/usr/bin/env python
from authomatic.providers import oauth2
from authomatic import Authomatic
import os

"""
Set arguements to use with gdocs.py:
	-URL is the location of the Google spreadsheet that will be converted.
	-top_level_key is the name of the top level key to set with the final json.
	-input_file is the location of the csv file you want to conver to json. 
	 This is optional if you set the --convertall flag, which will convert all
	 the csvs in the current directory.
	-output_file is the name of the final outputted json.
"""

top_level_key = "cards"
output_file = 'podcast.json'

COPY_GOOGLE_DOC_KEY = '1ySSgnYPjz3054EGxUDLiPffFb42dTpzY6R98jFCe-wQ'
COPY_PATH = 'data/copy.csv'

"""
OAUTH
"""

GOOGLE_OAUTH_CREDENTIALS_PATH = '~/.google_oauth_credentials'

authomatic_config = {
    'google': {
        'id': 1,
        'class_': oauth2.Google,
        'consumer_key': os.environ.get('GOOGLE_OAUTH_CLIENT_ID'),
        'consumer_secret': os.environ.get('GOOGLE_OAUTH_CONSUMER_SECRET'),
        'scope': ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/userinfo.email'],
        'offline': True,
    },
}

authomatic = Authomatic(authomatic_config, os.environ.get('AUTHOMATIC_SALT'))