import collections, itertools
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews, stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist

import re

from nltk.tokenize import RegexpTokenizer
from nltk.corpus.util import LazyCorpusLoader
from nltk.corpus.reader import *

import nltk.classify.util

import sys, os

pathname = os.path.dirname(sys.argv[0])        

nltk.data.path.append(os.path.abspath(pathname)+'/data'); 
movie_reviews = LazyCorpusLoader(
    sys.argv[1], CategorizedPlaintextCorpusReader,
    r'(?!\.).*\.txt', cat_pattern=r'(neg|pos)/.*',
    encoding='utf-8')

train_test_ratio = 3.0/4 
num_of_words = 10000

def best_word_feats(words):
    return dict([(word, True) for word in words if word in bestwords])
 
word_dist = FreqDist()
label_word_dist = ConditionalFreqDist()
 
for word in movie_reviews.words(categories=['pos']):
    word_dist[word] += 1;
    label_word_dist['pos'][word] += 1;
 
for word in movie_reviews.words(categories=['neg']):
    word_dist[word] += 1;
    label_word_dist['neg'][word] += 1;
 
pos_word_count = label_word_dist['pos'].N()
neg_word_count = label_word_dist['neg'].N()
total_word_count = pos_word_count + neg_word_count
 
word_scores = {}
 
for word, frequence in word_dist.iteritems():
    score_pos = BigramAssocMeasures.chi_sq(label_word_dist['pos'][word],
        (frequence, pos_word_count), total_word_count)
    score_neg = BigramAssocMeasures.chi_sq(label_word_dist['neg'][word],
        (frequence, neg_word_count), total_word_count)
    word_scores[word] = score_pos + score_neg 
 
best = sorted(word_scores.iteritems(), key=lambda (w,s): s, reverse=True)[:num_of_words]
bestwords = set([w for w, s in best])
 
print 'using naive bayes only on best %d words ' % num_of_words
 
files_in_neg = movie_reviews.fileids('neg')
files_in_pos = movie_reviews.fileids('pos')
 
neg_data = [(best_word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in files_in_neg]
pos_data = [(best_word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in files_in_pos]


negative_first_test_pos = int(len(neg_data)*train_test_ratio)
positive_first_test_pos = int(len(pos_data)*train_test_ratio)
 
train_data = neg_data[:negative_first_test_pos] + pos_data[:positive_first_test_pos]
test_data = neg_data[negative_first_test_pos:] + pos_data[positive_first_test_pos:]

print 'training on %d paragraphs and testing on %d paragraphs' % (len(train_data), len(test_data)) 
 
classifier = NaiveBayesClassifier.train(train_data)
 
print 'accuracy:', nltk.classify.util.accuracy(classifier, test_data)
classifier.show_most_informative_features(20)
 