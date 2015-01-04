#!/usr/bin/env python

from gdocs import GoogleDoc
import glob, subprocess, json, csv

url = 'https://docs.google.com/spreadsheet/ccc?key=0AkY5o_aAkwFydEctaXllbzlGUGRLanVQc0hSMlo5YXc'
    
def get_doc(url):
    if url == None:
        print colored('We need a Google Doc url', 'blue')
        return
    else:
        doc = {}
        bits = url.split('key=')
        bits = bits[1].split('&')
        doc['key'] = bits[0]

        g = GoogleDoc(**doc)
        g.get_auth()
        g.get_document()

def gdoc_to_json():
	for files in glob.glob("*.csv"):
		# print files
		subprocess.call('csvjson %s > output_csvkit.json' % files, shell=True)
		csv_to_json(files)

def csv_to_json(source):
	output = []
	with open(source) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			output.append(row)

	final_json = {'cards': output}
	
	with open('output.json', 'w') as outfile:
		json.dump(final_json, outfile)


if __name__ == "__main__":
	get_doc(url)
	gdoc_to_json()