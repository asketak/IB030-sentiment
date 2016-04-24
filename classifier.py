import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
 
train_test_ratio = 2.0/3
def words_in_sentence(words):
    return dict([(word, True) for word in words])
 
files_in_neg = movie_reviews.fileids('neg')
files_in_pos = movie_reviews.fileids('pos')
 
neg_data = [(words_in_sentence(movie_reviews.words(fileids=[f])), 'neg') for f in files_in_neg]
pos_data = [(words_in_sentence(movie_reviews.words(fileids=[f])), 'pos') for f in files_in_pos]
 
negative_first_test_pos = int(len(neg_data)*train_test_ratio)
positive_first_test_pos = int(len(pos_data)*train_test_ratio)
 
train_data = neg_data[:negative_first_test_pos] + pos_data[:positive_first_test_pos]
test_data = neg_data[negative_first_test_pos:] + pos_data[positive_first_test_pos:]
print 'training on %d paragraphs and testing on %d paragraphs' % (len(train_data), len(test_data))
 
classifier = NaiveBayesClassifier.train(train_data)
print 'accuracy:', nltk.classify.util.accuracy(classifier, test_data)
classifier.show_most_informative_features(20)
