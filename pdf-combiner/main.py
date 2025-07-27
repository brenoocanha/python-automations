import PyPDF2
import os

merger = PyPDF2.PdfMerger()

file_list = os.listdir("files")
file_list.sort()
print(file_list)

for file in file_list:
    if ".pdf" in file:
        merger.append(f"files/{file}")

merger.write("combined-pdfs.pdf")