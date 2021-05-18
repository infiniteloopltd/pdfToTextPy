import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
from io import BytesIO
import time
import urllib.request

#  python main.py ..url..

def pdfparser(url):
    print("Downloading from " + url)
    f = urllib.request.urlopen(url).read()
    fp = BytesIO(f)
    print("Downloaded")
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    for page in PDFPage.get_pages(fp):
        start_time = time.monotonic()
        interpreter.process_page(page)
        data =  retstr.getvalue()
        print('seconds per page: ', time.monotonic() - start_time)
    print("Complete")

if __name__ == '__main__':
    pdfparser(sys.argv[1])
