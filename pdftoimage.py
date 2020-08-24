from pdf2image import convert_from_path
import img2pdf
import tempfile
import os
import sys
import cv2
from tqdm import tqdm

#pdf_path='BOARD RESOLUTION SIRENA.pdf'
pdf_path='Head-First-Android-Development-2015.pdf'
with tempfile.TemporaryDirectory() as path:
    print("converting to images")
    images_from_path = convert_from_path(pdf_path, output_folder=path,fmt=".jpeg",paths_only=True,)
    print("Finished converting to images now inverting")
    dirname=path
    with open("name.pdf","wb") as f,tqdm(total=len(os.listdir(dirname)),file=sys.stdout) as pbar:
        imgs = []
        for fname in os.listdir(dirname):
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(dirname, fname)
            if os.path.isdir(path):
                continue
            #Mat=cv2.imread(path)
            #Mat=~Mat
            #cv2.imwrite(path,Mat,[int(cv2.IMWRITE_JPEG_QUALITY), 10])
            imgs.append(path)
            f.write(img2pdf.convert(imgs))
            pbar.update(1)

#images = convert_from_path("/home/sirena/Templates/BOARD RESOLUTION SIRENA.pdf")

