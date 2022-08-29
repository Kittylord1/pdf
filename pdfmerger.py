import PyPDF2

a = input('first pdfname')
b = input('second pdf name')
pdf1 = (f'./{a}')
pdf2 = (f'./{b}')
pdfs = (pdf1,pdf2)
def pdfcombiner(files):
    merger = PyPDF2.PdfFileMerger()
    for pdf in files:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')
pdfcombiner(pdfs)