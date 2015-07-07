# Google Doc to JSON

Just a quick python script that downloads a Google spreadsheet, converts it to json and then uploads it to a specified Amazon S3 bucket. Created to support a workflow that includes handlebars.js to display to the json on a site.

## Acknowledgements
oauth.py is reused from the [NPR App Template](https://github.com/nprapps/app-template), which is a great project you should check out and support. Additional inspiration from [Chris Keller](https://gist.github.com/chrislkeller/4700210), who wrote a post on a similar vein earlier this year. While none of the code here is from his project (just yet), it provided some pointers on where to head next. Specifically, don't write something into [csvkit](https://github.com/onyxfish/csvkit).

## How use it
Clone this repo to you local machine or download the files. I recommend starting a new python virtual environment, and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) for all your env needs.

This script relies on a number of Google and AWS environment variables and setting up oauth one first use, as laid out in the [NPR App Templates setup guide](http://blog.apps.npr.org/2014/09/08/how-to-setup-the-npr-app-template-for-you-and-your-news-org.html) and [oauth walk through](http://blog.apps.npr.org/2015/03/02/app-template-oauth.html). I set them all in my venv postactivate, but feel free to set them however works best for you (as long as do).

The values you need to set are:
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
APPS_GOOGLE_EMAIL
APPS_GOOGLE_PASS
GOOGLE_OAUTH_CLIENT_ID
GOOGLE_OAUTH_CONSUMER_SECRET
AUTHOMATIC_SALT
```

Additionally, within config.py set the key of the spreadsheet you want to convert, location and name of the file you want to create, and path t your s3 bucket.

Deploy code is handled by Fabric and kept in `fabfile.py`. Once everything is set, run `fab deploy` to download and convert the file, and then upload it to S3.