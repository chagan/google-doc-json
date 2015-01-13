#!/usr/bin/env python

"""
Set arguements to use with gdocs.py:
	-URL is the location of the Google spreadsheet that will be converted.
	-top_level_key is the name of the top level key to set with the final json.
	-input_file is the location of the csv file you want to conver to json. 
	 This is optional if you set the --convertall flag, which will convert all
	 the csvs in the current directory.
	-output_file is the name of the final outputted json.
"""

URL = 'https://docs.google.com/spreadsheet/ccc?key=1ySSgnYPjz3054EGxUDLiPffFb42dTpzY6R98jFCe-wQ'
top_level_key = "cards"
output_file = 'podcast.json'