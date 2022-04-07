from PyPDF2 import PdfFileWriter, PdfFileReader 

out = PdfFileWriter()
file = PdfFileReader('nem.pdf') # path to pdf file

num = file.numPages

for i in range(num):
    page = file.getPage(i)
    out.addPage(page)

password = 'pass'
out.encrypt(password)

with open('my_list', 'wb') as f:
    out.write(f)