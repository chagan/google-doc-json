#!/usr/bin/env python

import requests
from gdocs import GoogleDoc

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

if __name__ == "__main__":
	get_doc(url)