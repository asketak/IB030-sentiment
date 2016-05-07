import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

def words_in_sentence(words):
	return dict([(word, True) for word in words])
def best_word_feats(words,bestwords):
    return dict([(word, True) for word in words if word in bestwords])
def bigram_words_in_sentence(words, score_fn=BigramAssocMeasures.dice, n=200):
	bigram_finder = BigramCollocationFinder.from_words(words)
	bigrams = bigram_finder.nbest(score_fn, n)
	return dict([(ngram, True) for ngram in itertools.chain(words, bigrams)])