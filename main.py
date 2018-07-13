import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import string

pdffile = open('JavaBasics-notes.pdf', 'rb')
# rb because pdfs are binary files

reader = PyPDF2.PdfFileReader(pdffile)

num_pages = reader.numPages

all_string = ''

# num pages - 2 is used to loop over as the last two pages are blank
for pages in range(num_pages - 2):
    page = reader.getPage(pages)
    add = page.extractText()
    all_string += add

all_string = all_string.lower()

words = word_tokenize(all_string)
count = 0

stop_words = set(stopwords.words("english"))


filtered = [word for word in words if not word in stop_words]
filtered = [word for word in filtered if not word in set(string.punctuation)]

print(filtered)

freq = nltk.FreqDist(filtered)

print(freq.most_common(1000))
























