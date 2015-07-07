#!/usr/bin/env python
from authomatic.providers import oauth2
from authomatic import Authomatic
import os

"""
Set arguements to use with oauth.py:
	* TOP_LEVEL_KEY is the name of the top level key to set with the final json.
	* OUTPUT_FILE is the name of the final outputted json.
	* COPY_GOOGLE_DOC_KEY is key for google doc to download
	* COPY_PATH is location to save downloaded csv
	* S3_PATH is path to S3 bucket to upload json to

	See README for instructions on setting up oauth
"""

TOP_LEVEL_KEY = "cards"
OUTPUT_FILE = 'podcast.json'

COPY_GOOGLE_DOC_KEY = '1ySSgnYPjz3054EGxUDLiPffFb42dTpzY6R98jFCe-wQ'
COPY_PATH = 'data/copy.csv'
S3_PATH = 's3://wbez-assets/podcast-static/'

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