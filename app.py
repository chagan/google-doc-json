#!/usr/bin/env python

from flask import Flask, make_response, render_template, request
import google_doc_json as gdocjson
import config
from fabric.api import local
from fabfile import deploy


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        try:
            gdocjson.get_doc(config.URL)
            gdocjson.gdoc_to_json()
            #deploy()

        except Exception as e:
            return "There was a problem. % s" % e
        else:
            return "Podcasts updated"

if __name__ == '__main__':

    app.run(debug=True, port=8081)