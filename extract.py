import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tabulate import tabulate
import nltk
import string
import matplotlib.pyplot as plt
import numpy as np
plt.rcdefaults()


def extract_text_from_pdf(filename):
    """
    Converts PDF text data to string.

    Parameters:
    file path (str): path to the pdf file to be used

    Returns:
    str: cll the text obtained from the pdf
    """

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
    """
       Filters the String provided .

        Removes Stopwords(via NLTK), Punctuations and other Non-Keywords not in the NLTK

       Parameters:
       text to be filtered (str)

       Returns:
       (x, y) Keywords and Frequency (List of Tuples(len = 2))

       """

    all_string = all_string.lower()

    removers = ['all', 'rights', 'reserved', 'basics', 'jguru.com', '1996-2003', '.java', '©', '//', "''", "``", '...', '/*',
                '==', '--', '1', '5', '3', '2', '0']
    for remove in removers:
        all_string = all_string.replace(remove, '')

    words = word_tokenize(all_string)

    stop_words = set(stopwords.words("english"))

    filtered = [word for word in words if not word in stop_words]
    filtered = [word for word in filtered if not word in set(string.punctuation)]

    freq = nltk.FreqDist(filtered)

    keywords = freq.most_common(40)

    # eliminating any stopwords left
    del keywords[2:4]
    del keywords[7]

    return keywords[:]


def plot(keywords):
    """
       Plots a Bar graph of Words to their Frequency.

       Parameters:
       (x, y) Coordinates (List of Tuples(len = 2))

       Returns:
       Bar graph (png) and List of Coordinates(x, y)

       """

    x = []
    y = []

    #deleating new as its not a keyword
    del keywords[1]

    for keyword in keywords:
        tempx = keyword[0]
        tempy = keyword[1]
        x.append(tempx)
        y.append(tempy)

    y_pos = np.arange(len(x))

    plt.bar(y_pos, y, align='center', alpha=0.5)
    plt.xticks(y_pos, tuple(x))
    plt.ylabel('Frequency')
    plt.title('Keywords in the Documents')

    plt.show()


def main():
    #
    filename = 'JavaBasics-notes.pdf'
    text = extract_text_from_pdf(filename=filename)
    keywords = filter_data(text)
    plot(keywords[:12])
    del keywords[1]
    for keyword in keywords:
        list(keyword)
    print(tabulate(keywords, headers=['Keyword', 'Frequency']))


if __name__ == '__main__':
    main()