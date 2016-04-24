import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
 
train_test_ratio = 2.0/3

def bigram_words_in_sentence(words, score_fn=BigramAssocMeasures.dice, n=200):
	bigram_finder = BigramCollocationFinder.from_words(words)
	bigrams = bigram_finder.nbest(score_fn, n)
	return dict([(ngram, True) for ngram in itertools.chain(words, bigrams)])
 
 
files_in_neg = movie_reviews.fileids('neg')
files_in_pos = movie_reviews.fileids('pos')
 
neg_data = [(bigram_words_in_sentence(movie_reviews.words(fileids=[f])), 'neg') for f in files_in_neg]
pos_data = [(bigram_words_in_sentence(movie_reviews.words(fileids=[f])), 'pos') for f in files_in_pos]
 
negative_first_test_pos = int(len(neg_data)*train_test_ratio)
positive_first_test_pos = int(len(pos_data)*train_test_ratio)
 
train_data = neg_data[:negative_first_test_pos] + pos_data[:positive_first_test_pos]
test_data = neg_data[negative_first_test_pos:] + pos_data[positive_first_test_pos:]
print 'training on %d paragraphs and testing on %d paragraphs' % (len(train_data), len(test_data))
 
classifier = NaiveBayesClassifier.train(train_data)
print 'accuracy:', nltk.classify.util.accuracy(classifier, test_data)
classifier.show_most_informative_features(20)