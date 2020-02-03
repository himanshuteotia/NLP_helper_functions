
## Install and import all the necessary libraries
#!pip install PyPDF2
import PyPDF2
from PyPDF2 import PdfFileReader


## Extracting text from PDF file

#Creating a pdf file object
pdf = open("file.pdf","rb")


#creating pdf reader object
pdf_reader = PyPDF2.PdfFileReader(pdf)

#checking number of pages in a pdf file
print(pdf_reader.numPages)

#creating a page object
page = pdf_reader.getPage(0)

#finally extracting text from the page
print(page.extractText())

#closing the pdf file
pdf.close()



#### Please note that the function above doesn’t work for scanned PDFs. ###

