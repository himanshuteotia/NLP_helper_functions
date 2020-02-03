
'''
The procedure of converting raw text data into machine
understandable format (numbers) is called feature engineering of text data. Machine learning and deep learning algorithms’ performance and
accuracy is fundamentally dependent on the type of feature engineering
technique used

'''

## Converting Text to Features Using One Hot Encoding

'''
The traditional method used for feature engineering is One Hot encoding.
If anyone knows the basics of machine learning, One Hot encoding is
something they should have come across for sure at some point of time or
maybe most of the time. It is a process of converting categorical variables
into features or columns and coding one or zero for the presence of that
particular category. We are going to use the same logic here, and the
number of features is going to be the number of total tokens present in the
whole corpus.

'''

Text = "I am learning NLP"

# Importing the library
import pandas as pd

# Generating the features
pd.get_dummies(Text.split())

# Output has 4 features since the number of distinct words present in the input was 4.


## Converting Text to Features Using Count Vectorizing
'''
The approach one hot encoding has a disadvantage. It does not take the
frequency of the word occurring into consideration. If a particular word
is appearing multiple times, there is a chance of missing the information
if it is not included in the analysis. A count vectorizer will solve that
problem.
In this recipe, we will see the other method of converting text to
feature, which is a count vectorizer.

'''

#importing the function
from sklearn.feature_extraction.text import CountVectorizer
# Text
text = ["I love NLP and I will learn NLP in 2month "]
# create the transform
vectorizer = CountVectorizer()

# tokenizing
vectorizer.fit(text)
# encode document
vector = vectorizer.transform(text)

# summarize & generating output
print(vectorizer.vocabulary_)
# The fifth token nlp has appeared twice in the document.
print(vector.toarray())


## Generating N-grams

'''
If you observe the above methods, each word is considered as a feature.
There is a drawback to this method.
It does not consider the previous and the next words, to see if that
would give a proper and complete meaning to the words.
For example: consider the word “not bad.” If this is split into individual
words, then it will lose out on conveying “good” – which is what this word
actually means.
As we saw, we might lose potential information or insight because a
lot of words make sense once they are put together. This problem can be
solved by N-grams.
N-grams are the fusion of multiple letters or multiple words. They are
formed in such a way that even the previous and next words are captured.

• Unigrams are the unique words present in the sentence.
• Bigram is the combination of 2 words.
• Trigram is 3 words and so on.

For example,
“I am learning NLP”
Unigrams: “I”, “am”, “ learning”, “NLP”
Bigrams: “I am”, “am learning”, “learning NLP”
Trigrams: “I am learning”, “am learning NLP”

'''

Text = "I am learning NLP"

#Import textblob
from textblob import TextBlob
#For unigram : Use n = 1
TextBlob(Text).ngrams(1)

#For Bigram : For bigrams, use n = 2
TextBlob(Text).ngrams(2)


# Bigram-based features for a document

'''

Just like in the last recipe, we will use count vectorizer to generate features.
Using the same function, let us generate bigram features and see what the
output looks like.

'''

#importing the function
from sklearn.feature_extraction.text import CountVectorizer
# Text
text = ["I love NLP and I will learn NLP in 2month "]
# create the transform
vectorizer = CountVectorizer(ngram_range=(2,2))
# tokenizing
vectorizer.fit(text)

# encode document
vector = vectorizer.transform(text)
# summarize & generating output
print(vectorizer.vocabulary_)
print(vector.toarray())

## Generating Co-occurrence Matrix
'''
one more method of feature engineering called a co-­
occurrence matrix. A co-occurrence matrix is like a count vectorizer where it counts the
occurrence of the words together, instead of individual words.
'''

import numpy as np
import nltk
from nltk import bigrams
import itertools

# Create function for co-occurrence matrix

def co_occurrence_matrix(corpus):
    vocab = set(corpus)
    vocab = list(vocab)
    vocab_to_index = { word:i for i, word in enumerate(vocab) }
    # Create bigrams from all words in corpus
    bi_grams = list(bigrams(corpus))
    # Frequency distribution of bigrams ((word1, word2),num_occurrences)
    bigram_freq = nltk.FreqDist(bi_grams).most_common(len(bi_grams))
    # Initialise co-occurrence matrix
    # co_occurrence_matrix[current][previous]
    co_occurrence_matrix = np.zeros((len(vocab), len(vocab)))
    # Loop through the bigrams taking the current and previous word,
    # and the number of occurrences of the bigram.
    for bigram in bigram_freq:
        current = bigram[0][1]
        previous = bigram[0][0]
        count = bigram[1]
        pos_current = vocab_to_index[current]
        pos_previous = vocab_to_index[previous]
        co_occurrence_matrix[pos_current][pos_previous] = count
    co_occurrence_matrix = np.matrix(co_occurrence_matrix)
    # return the matrix and the index
    return co_occurrence_matrix,vocab_to_index

sentences = [['I', 'love', 'nlp'],
                   ['I', 'love','to' 'learn'],
                   ['nlp', 'is', 'future'],
                   ['nlp', 'is', 'cool'],["my","name","is","Himanshu"]]

# create one list using many lists
merged = list(itertools.chain.from_iterable(sentences))
matrix,vocab_to_index = co_occurrence_matrix(merged)

print(matrix)
# generate the matrix
CoMatrixFinal = pd.DataFrame(matrix[0], index=vocab_to_index,columns=vocab_to_index)
print(CoMatrixFinal)



## Hash Vectorizing
'''
A count vectorizer and co-occurrence matrix have one limitation though.
In these methods, the vocabulary can become very large and cause
memory/computation issues.
One of the ways to solve this problem is a Hash Vectorizer.

Hash Vectorizer is memory efficient and instead of storing the tokens
as strings, the vectorizer applies the hashing trick to encode them as
numerical indexes. The downside is that it’s one way and once vectorized,
the features cannot be retrieved.

'''

from sklearn.feature_extraction.text import HashingVectorizer
# list of text documents
text = ["The quick brown fox jumped over the lazy dog."]

# Generate hash vectorizer matrix

#Let’s create the HashingVectorizer of a vector size of 10.
# transform
vectorizer = HashingVectorizer(n_features=10)
# create the hashing vector
vector = vectorizer.transform(text)
# summarize the vector
print(vector.shape)
print(vector.toarray())
#It created vector of size 10 and now this can be used for any supervised/unsupervised tasks.