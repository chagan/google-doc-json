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
	local( "aws s3 sync data %s --exclude *.tmp --exclude *.csv" % config.S3_PATH)

def csv_to_json(source):
	output = []
	with open(source) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			output.append(row)

	final_json = {config.TOP_LEVEL_KEY: output}
	new_file = "data/%s" % config.OUTPUT_FILE
	backup_file = "data/backup-%s" % config.OUTPUT_FILE
	if os.path.exists(new_file):
		os.rename(new_file, backup_file)
	
	with open(new_file, 'w') as outfile:
		json.dump(final_json, outfile)