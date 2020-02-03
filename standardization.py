## Create a custom lookup dictionary

lookup_dict = {'nlp':'natural language processing',
'ur':'your', "wbu" : "what about you"}

import re

##  Create a custom function for text standardization

def text_std(input_text):
    words = input_text.split()
    new_words = []
    for word in words:
        word = re.sub(r'[^\w\s]','',word)
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
            new_words.append(word)
            new_text = " ".join(new_words)
    return new_text

text_std("I like nlp it's ur choice")

##  Correcting Spelling

text=['Introduction to NLP','It is likely to be useful, to people ','Machine learning is the new electrcity', 'R is good langauage','I like this book','I want more books like this']


#convert list to dataframe
import pandas as pd
df = pd.DataFrame({'tweet':text})
print(df)

## Execute below code on the text data

#Install textblob library
#!pip install textblob

#import libraries and use 'correct' function
from textblob import TextBlob

df['tweet'].apply(lambda x: str(TextBlob(x).correct()))


#we can also use autocorrect library as shown below

#install autocorrect
#!pip install autocorrect

### important file ruwiki-latest-pages-articles.xml.bz2

from autocorrect import Speller
spell = Speller(lang='en')
print(spell("I'm not sleapy and tehre is no place I'm giong to."))


## Tokenizing Text

#The simplest way to do this is by using the TextBlob library.

#convert list to dataframe
import pandas as pd
df = pd.DataFrame({'tweet':text})
print(df)

#Execute below code on the text data
from textblob import TextBlob
TextBlob(df['tweet'][3]).words

## Stemming

text=['I like fishing','I eat fish','There are many fishes in pound']

#convert list to dataframe
import pandas as pd
df = pd.DataFrame({'tweet':text})
print(df)

#Import library
from nltk.stem import PorterStemmer

st = PorterStemmer()
df['tweet'][:5].apply(lambda x: " ".join([st.stem(word) for
word in x.split()]))


## Lemmatizing

'''
Lemmatization is a process of
extracting a root word by considering the vocabulary. For example, “good,”
“better,” or “best” is lemmatized into good.

The part of speech of a word is determined in lemmatization. It will
return the dictionary form of a word, which must be a valid word while
stemming just extracts the root word.

• Lemmatization handles matching “car” to “cars” along
with matching “car” to “automobile.”
• Stemming handles matching “car” to “cars.”


Lemmatization can get better results.
• The stemmed form of leafs is leaf.
• The stemmed form of leaves is leav.
• The lemmatized form of leafs is leaf.
• The lemmatized form of leaves is leaf.
'''

#Import library
from textblob import Word

text=['I like fishing','I eat fish','There are many fishes in pound', 'leaves and leaf']
#Code for lemmatize

#convert list to dataframe
import pandas as pd
df = pd.DataFrame({'tweet':text})

#Import library
from textblob import Word
#Code for lemmatize
df['tweet'] = df['tweet'].apply(lambda x: " ".join([Word(word).
lemmatize() for word in x.split()]))
df['tweet']