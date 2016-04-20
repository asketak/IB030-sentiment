import urllib
from bs4 import BeautifulSoup

for x in range(1,100):
	#parser = MyHTMLParser()
	url = "http://www.csfd.cz/komentare/strana-" + `x` + "/"
	response = urllib.urlopen(url)
	data = response.read()      # a `bytes` object
	text = data.decode('utf-8') # a `str`; this step can't be used if data is binaryo
	text = unicode(text).encode('utf8')
	#print(text)
	soup = BeautifulSoup(text, 'html')
	for post in soup.find_all('div', attrs={'class': 'post'}):
		print "rating/comment section"
		rating = post.find('img', attrs={'class': 'rating'})
		comment = post.find('p' )
		print(rating)
		print(comment)
		print("-------------------")
#    bar = foo.find('div', attrs={'class': 'bar'})
