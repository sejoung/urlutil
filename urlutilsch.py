# -*- coding: utf-8 -*-
import urllib2
import sys
import schedule
import time
from datetime import datetime as dt

def now_str():
    return dt.now().time().strftime("%H:%M:%S")

def call_url_download_file():
	url = sys.argv[1]
	filepath = sys.argv[2]
	f = open(filepath, 'wb')
	response = urllib2.urlopen(url)
	f.write(response.read())
	response.close()
	f.close()
	print('RUNNING: {0} {1}'.format(now_str(), filepath))

if len(sys.argv) > 2:
	print('START: {0}'.format(now_str()))
	schedule.every(1).minutes.do(call_url_download_file)
	while 1:
		schedule.run_pending()
else:
	print("no arg")
	print("urlutil [url] [filepath]")
	print("ex) urlutil http://www.naver.com C:/main.html")
