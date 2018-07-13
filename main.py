import PyPDF2

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
    print(add)
