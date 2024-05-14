from pdf2docx import Converter

pdf_path = "sample.pdf"
docx_path = "sample.docx"

Cv=Converter(pdf_path)
Cv.convert(docx_filename=docx_path)
Cv.close()