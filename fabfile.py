#!/usr/bin/env python

from fabric.api import local
import oauth
import config
import csv
import os
import json

def deploy():
	oauth.get_document(config.COPY_GOOGLE_DOC_KEY, config.COPY_PATH)
	csv_to_json(config.COPY_PATH)
	local( "aws s3 sync data s3://wbez-assets/podcast-static/ --exclude *.tmp --exclude *.csv" )

def csv_to_json(source):
	output = []
	with open(source) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			output.append(row)

	final_json = {config.top_level_key: output}
	newfile = "data/%s" % config.output_file
	oldfile = "data/old-%s" % config.output_file
	if os.path.exists('/this/is/a/dir'):
		os.rename(newfile, oldfile)
	
	with open(newfile, 'w') as outfile:
		json.dump(final_json, outfile)