from __future__ import print_function
import urllib
from bs4 import BeautifulSoup
import re
import sys

import time
from functools import wraps


def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.

    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck, e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

@retry(Exception, tries=8, delay=3, backoff=2)
def send(url):
	return urllib.urlopen(url)

for x in range(2,10000):
	url = "http://www.csfd.cz/komentare/strana-" + `x` + "/"
	response = send(url)
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
