#!/usr/bin/env python

from fabric.api import local

def deploy():
	local( "aws s3 sync data s3://app-test-assets/ --exclude *.tmp" )