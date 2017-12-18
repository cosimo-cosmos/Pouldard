import os, sys
from datetime import datetime
import re
from multiprocessing import Pool
from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io
from PyPDF2 import PdfFileReader, PdfFileWriter
import tqdm

test_dir = r"C:\TEMP\test"
Input_dir = r"C:\TEMP\Pouldard\Input_dir"
Ouput_dir = r"C:\TEMP\Pouldard\Output_dir\\"
#Input_dir_temp = r"C:\TEMP\Pouldard\Input_dir_temp"
"""

#split pdf on 10 units chunk
for j, file in enumerate(os.listdir(test_dir)):
    pdf_file = str(os.path.join(os.path.abspath(test_dir), file))


    def split_pdf_chunck(input_pdf):

        pdf = PdfFileReader(open(input_pdf, 'rb'))
        w = PdfFileWriter()


        for i in range(10):

            w.addPage(pdf.getPage(i))

        with open(Input_dir +'input{}.pdf'.format(j), 'wb') as outfile:
            w.write(outfile)
            #return outfile
    split_pdf_chunck(pdf_file)
"""
def get_pdf_paths(folder):
    return(os.path.join(folder, file)
        for file in sorted(os.listdir(folder), key = lambda x: (int(re.sub('\D','',x)),x)))


#pdf_files = get_pdf_paths(Input_dir)

#OCR PDF and return str i/O(put into docstring at the end)
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


    with open(Ouput_dir + 'output{0:%H_%M_%S.%f}.txt'.format(datetime.now()), 'w', encoding='utf-8') as f:

        for item in final_text:
            f.write(item)
    return input_pdf


"""
def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))
pdf_file =absoluteFilePaths(Input_dir)
"""

#print(next(absoluteFilePaths(Input_dir)))
"""
p.imap_unordered(extract_text, pdf_file)
p.close()
p.join()
"""






if __name__=='__main__':
    pdf_files = get_pdf_paths(Input_dir)
    sys.stdout = open('C:\TEMP\Pouldard\Input_as_coming_list.txt','w')

    p = Pool()
    for fn in p.imap_unordered(extract_text, pdf_files):
        print(fn)
    #p.map(extract_text, pdf_files)
    p.close()
    p.join()









