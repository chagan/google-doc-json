#!/usr/bin/env python

from gdocs import GoogleDoc
import glob, subprocess, json, csv, argparse, config


parser = argparse.ArgumentParser()
parser.add_argument('--convertall', '-c', action='store_true', help='Convert all csv in a folder to json' )
parser.add_argument('--input', '-i', help='Input csv file if not using a GoogleDoc' )
args = parser.parse_args()
    
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

def csv_to_json(source):
	output = []
	with open(source) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			output.append(row)

	final_json = {config.top_level_key: output}
	
	with open(config.output_file, 'w') as outfile:
		json.dump(final_json, outfile)

def gdoc_to_json():
	if args.convertall:
		for files in glob.glob("*.csv"):
			csv_to_json(files)
	elif args.input:
		csv_to_json(args.input)
	else:
		print 'We need a csv file. Convert a Google doc or specify a local file with the -i flag'
        return


if __name__ == "__main__":
	get_doc(config.URL)
	gdoc_to_json()