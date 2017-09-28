from PyPDF2 import PdfFileMerger, PdfFileReader


files = []
while True:
	files.append(input("filename: "))
	if input("add more files? ") != "y":
		break

merger = PdfFileMerger()
for f in files:
	merger.append(PdfFileReader(f, 'rb'))
    

merger.write("output.pdf")