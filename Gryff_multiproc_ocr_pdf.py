from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io
from PyPDF2 import PdfFileReader, PdfFileWriter
#import tqdm
#pdf_file = r"C:\TEMP\Pouldard\numpy_coockboock_cover.pdf"
#pdf_file = r"C:\TEMP\Test_wip\title_test.pdf"
pdf_file = r"C:\TEMP\test\1b86d841b9e46a4c11b473e9abc06f32.pdf"

#split pdf on 10 units chunk

def split_pdf_chunck(input_pdf):

    pdf = PdfFileReader(open(input_pdf, 'rb'))
    w = PdfFileWriter()


    for i in range(10):

        w.addPage(pdf.getPage(i))

    with open('output.pdf', 'wb') as outfile:
        w.write(outfile)
        return outfile
split_pdf_chunck(pdf_file)

"""
#OCR PDF and return str i/O
def extract_text(input_pdf):
   
    tool = pyocr.get_available_tools()[0]
    lang = tool.get_available_languages()[0]

    req_image = []
    final_text = []

    image_pdf = Image(filename=input_pdf, resolution=300)
    image_jpeg = image_pdf.convert('jpeg')

    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))

    for img in req_image:
        txt = tool.image_to_string(
            PI.open(io.BytesIO(img)),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        final_text.append(txt)
    return final_text

print(extract_text(pdf_file))
"""