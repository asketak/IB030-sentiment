import urllib

for x in range(1,10):
	url = "http://www.csfd.cz/komentare/strana-" + `x` + "/"
	response = urllib.urlopen(url)
	data = response.read()      # a `bytes` object
	text = data.decode('utf-8') # a `str`; this step can't be used if data is binaryo
	text = unicode(text).encode('utf8')
	print "START OT TEXT"
	print "%s" % text
