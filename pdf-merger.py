#!i/usr/bin/env python3
"""
I got sick of needing to merge pdfs so I made a script to do it for me
Maybe over complicating things with the structure but whatever
"""
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

import PyPDF2


def getFiles():
    """Get filenames via tkinter and return them"""
    Tk().withdraw()
    filenames = askopenfilenames()
    return filenames


def merge_pdfs(pdfs):
    """Merge pdfs provided"""
    filename = "merged_pdf.pdf"
    merger = PyPDF2.PdfWriter()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(filename)
    print("Created: ", filename)


if __name__ == '__main__':
    pdfs = getFiles()
    print("Merging PDFS: ", *pdfs)
    merge_pdfs(pdfs)
