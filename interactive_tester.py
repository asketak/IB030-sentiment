import re

from nltk.tokenize import RegexpTokenizer
from nltk.corpus.util import LazyCorpusLoader
from nltk.corpus.reader import *

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

import sys, os
import cPickle

from feats import *

print "loading feats function\n"

savefile = open('feats.pickle', 'r')
feats = cPickle.load(savefile)

print "loading classifier\n"

savefile = open('classifier.pickle', 'r')
classifier = cPickle.load(savefile)

print "finished loading\n"

while True:
	response = raw_input("Please enter sentence you want to classify, or press enter to end:\n")
	f = feats(response.split())
	print 'result:', classifier.classify(f)
	if len(response) == 0:
		break
