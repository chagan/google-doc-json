#Google Doc to JSON

Just a quick python script that downloads a Google spreadsheet, converts it to json and then uploads it to a specified Amazon S3 bucket. Created to support a workflow that includes handlebars.js to display to the json on a site.

## Acknowledgements
Gdocs.py is reused from the [NPR App Template](https://github.com/nprapps/app-template), which is a great project you should check out and support. Additional inspiration from [Chris Keller](https://gist.github.com/chrislkeller/4700210), who wrote a post on a similar vein earlier this year. While none of the code here is from his project (just yet), it provided some pointers on where to head next. Specicifically, don't write something into [csvkit](https://github.com/onyxfish/csvkit).

## How use it
Clone this repo to you local machine or download the files. I recommend starting a new python virtual environment, and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) for all your env needs.

This script relies on a number of environment variables, as laid out in the [NPR App Template](http://blog.apps.npr.org/2014/09/08/how-to-setup-the-npr-app-template-for-you-and-your-news-org.html). I set them all in my venv postactivate, but feel free to set them however works best for you (as long as do).

The values you need to set:
```
AWS_ACCESS_KEY_ID=[YourAWSAccessKey]
AWS_SECRET_ACCESS_KEY=[YourAWSSecretKey]
AWS_DEFAULT_REGION=[aws-regon] (ex. us-east-1)
APPS_GOOGLE_EMAIL='youremail@gmail.com'
APPS_GOOGLE_PASS='notARealPassword'
```

Additionally, within google-doc-json.py set the url of the spreadsheet you wan to convert and location and name of the file you wanto create.

Currently the workflow is to run google-doc-json.py to download and conver the file, then use fabric to upload it to S3. So in your commandline you would run:
```
python google-doc-json.py
fab deploy
```