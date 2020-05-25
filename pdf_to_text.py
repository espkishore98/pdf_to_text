import PyPDF2

pdfFileObj = open('pypdf1.pdf', 'rb')
pdfReader =PyPDF2.PdfFileReader(pdfFileObj)
x=pdfReader.numPages
print(x)
for i in range(0, x+1 ):
    pageObj = pdfReader.getPage(i)
    text=pageObj.extractText()
    file1=open(r"I:\All\P\python practise\1.txt","a")
    file1.writelines(text)
    file1.close()