#Importing data
import nltk
#nltk.download()
from nltk.corpus import webtext
nltk.download('webtext')
wt_sentences = webtext.sents('firefox.txt')
wt_words = webtext.words('firefox.txt')

#Import necessary libraries
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

#Check number of words in the data

len(wt_sentences)
len(wt_words)


## Compute the frequency of all words in the reviews

frequency_dist = nltk.FreqDist(wt_words)
frequency_dist

sorted_frequency_dist =sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)
sorted_frequency_dist

 ## Consider words with length greater than 3 and plot

large_words = dict([(k,v) for k,v in frequency_dist.items() if
len(k)>3])

frequency_dist = nltk.FreqDist(large_words)
frequency_dist.plot(50,cumulative=False)

## Build Wordcloud

'''
Wordcloud is the pictorial representation of the most frequently repeated
words representing the size of the word.
'''

#install library
# !pip install wordcloud

#build wordcloud
from wordcloud import WordCloud
wcloud = WordCloud().generate_from_frequencies(frequency_dist)

#plotting the wordcloud
import matplotlib.pyplot as plt
plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off")
(-0.5, 399.5, 199.5, -0.5)
plt.show()
