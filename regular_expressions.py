
## Tokenizing
'''
You want to split the sentence into words – tokenize. One of the ways to do
this is by using re.split.
'''

# Import library
import re

#run the split query
re.split('\s+','I like this book.')


## Extracing email IDs

doc = "For more details please mail us at: xyz@abc.com,pqr@mno.com"

addresses = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
for address in addresses:
    print(address)


## Replacing email IDs

doc = "For more details please mail us at xyz@abc.com"
new_email_address = re.sub(r'([\w\.-]+)@([\w\.-]+)',r'pqr@mno.com', doc)
print(new_email_address)


## Extract data from the ebook and perform regex

# Import library
import re
import requests
#url you want to extract
url = 'https://www.gutenberg.org/files/2638/2638-0.txt'
#function to extract
def get_book(url):
     # Sends a http request to get the text from project Gutenberg
    raw = requests.get(url).text
    # Discards the metadata from the beginning of the book
    start = re.search(r"\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .* \*\*\*",raw ).end()
    # Discards the metadata from the end of the book
    stop = re.search(r"II", raw).start()
    # Keeps the relevant text
    text = raw[start:stop]
    return text

# processing
def preprocess(sentence):
    return re.sub('[^A-Za-z0-9.]+' , ' ', sentence).lower()

#calling the above function
book = get_book(url)
processed_book = preprocess(book)
print(processed_book)

## Perform some exploratory data analysis on this data using regex

# Count number of times "the" is appeared in the book
len(re.findall(r'the', processed_book))

#Replace "i" with "I"
processed_book = re.sub(r'\si\s', " I ", processed_book)
print(processed_book)