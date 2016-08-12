# -*- coding: utf-8 -*-
import urllib2
import sys

def call_url_download_file(url, filename):
    f = open(filename, 'wb')
    response = urllib2.urlopen(url)
    f.write(response.read())
    response.close()
    f.close()

if len(sys.argv) > 2:
    call_url_download_file(sys.argv[1], sys.argv[2])
else:
    print("no arg")
    print("urlutil [url] [filepath]")
    print("ex) urlutil http://www.naver.com C:/main.html")
