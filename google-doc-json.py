#!/usr/bin/env python

from gdocs import GoogleDoc
import glob, subprocess

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
		print files
		subprocess.call('csvjson %s > output.json' % files, shell=True) 


if __name__ == "__main__":
	get_doc(url)
	gdoc_to_json()