from __future__ import print_function
import urllib
from bs4 import BeautifulSoup
import re
import sys

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

for x in range(2,10000):
	url = "http://www.csfd.cz/komentare/strana-" + `x` + "/"
	response = urllib.urlopen(url)
	data = response.read()      # a `bytes` object
	text = data.decode('utf-8') # a `str`; this step can't be used if data is binaryo
	text = unicode(text).encode('utf8')
	warning(x)
	soup = BeautifulSoup(text, 'html')
	for post in soup.find_all('div', attrs={'class': 'post'}):
		rating = post.find('img', attrs={'class': 'rating'})

		if rating is not None: # Found img
			rating = rating.get('src')
			rating = rating[-5]
		if rating is None: # not found img
			rating = post.find('strong', attrs={'class': 'rating'})
			if rating is not None: # odpad
				rating = '0'
			else:
				rating = None # neni rating

		if rating is not None:
			comment = unicode(post.find('p').getText()).encode('utf8').replace('\n', ' ').replace('\r', '')
			print(rating + ' , ' + comment)
