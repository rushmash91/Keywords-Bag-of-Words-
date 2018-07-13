import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import string
import matplotlib.pyplot as plt
import numpy as np
plt.rcdefaults()


def extract_text_from_pdf(filename):
    pdffile = open(filename, 'rb')
    # rb because pdfs are binary files

    reader = PyPDF2.PdfFileReader(pdffile)

    num_pages = reader.numPages

    all_string = ''

    # num pages - 2 is used to loop over as the last two pages are blank
    for pages in range(num_pages - 2):
        page = reader.getPage(pages)
        add = page.extractText()
        all_string += add
    return all_string


def filter_data(all_string):
    all_string = all_string.lower()

    removers = ['all', 'rights', 'reserved', 'basics', 'jguru.com', '1996-2003', '.java', '©', '//', "''", "``", '...', '/*',
                '==', '--', '1', '5', '3', '2']
    for remove in removers:
        all_string = all_string.replace(remove, '')

    words = word_tokenize(all_string)

    stop_words = set(stopwords.words("english"))

    filtered = [word for word in words if not word in stop_words]
    filtered = [word for word in filtered if not word in set(string.punctuation)]

    freq = nltk.FreqDist(filtered)

    keywords = freq.most_common(40)
    del keywords[2:4]
    del keywords[7]
    return keywords


def plot(keywords):
    x = []
    y = []

    for keyword in keywords:
        tempx = keyword[0]
        tempy = keyword[1]
        x.append(tempx)
        y.append(tempy)

    print(x)
    print(y)
    y_pos = np.arange(len(x))

    plt.bar(y_pos, y, align='center', alpha=0.5)
    plt.xticks(y_pos, tuple(x))
    plt.ylabel('Frequency')
    plt.title('Keywords in the Documents')

    plt.show()


def main():
    filename = 'JavaBasics-notes.pdf'
    text = extract_text_from_pdf(filename=filename)
    keywords = filter_data(text)
    plot(keywords[:12])


if __name__ == '__main__':
    main()