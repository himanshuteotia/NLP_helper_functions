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
