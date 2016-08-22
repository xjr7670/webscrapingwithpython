#!/usr/bin/env python3

from urllib.request import urlopen
from io import StringIO
from io import open
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPDF(pdfFile)

print(outputString)
pdfFile.close()
