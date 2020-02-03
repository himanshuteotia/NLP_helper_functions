#Step 1 Install and import all the necessary libraries
# !pip install bs4
import urllib.request as urllib2
from bs4 import BeautifulSoup


# Step 2 Fetch the HTML file
'''
Pick any website from the web that you want to extract. Let’s pick
Wikipedia for this example.

'''

response = urllib2.urlopen('https://www.voanews.com/science-health/china-reports-bird-flu-outbreak-hunan-province')
html_doc = response.read()


# Step 3 Parse the HTML file

#Parsing
soup = BeautifulSoup(html_doc, 'html.parser')
# Formating the parsed html file
strhtm = soup.prettify()
# Print few lines
print (strhtm[:1000])


# Step 4 Extracting tag value

print(soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)


# Step 5 Extracting all instances of a particular tag

#for x in soup.find_all('a'): print(x.string)


#Step 6 Extracting all text of a particular tag

for x in soup.find_all('p'): print(x.text)