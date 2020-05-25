import PyPDF2

pdfFileObj = open('pypdf1.pdf', 'rb')
pdfReader =PyPDF2.PdfFileReader(pdfFileObj)
x=pdfReader.numPages//counting number of pages in file
print(x)//displays total page number in file
for i in range(0, x+1 ):
    pageObj = pdfReader.getPage(i)//gets page number from file
    text=pageObj.extractText()//it will extract text and places to variable
    file1=open(r"I:\All\P\python practise\1.txt","a")//place the directory link where you want to download the text file, a is the command used to append extracted text in text file
    file1.writelines(text)
    file1.close()
