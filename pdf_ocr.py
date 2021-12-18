# import libraries
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os

# path to the pdf
PDF_file = 'UE.pdf'

pages = convert_from_path(PDF_file)

image_counter = 1

for page in pages:
    # Declaring filename for each page of PDF as JPG
    filename = "page_" + str(image_counter) + ".jpg"
    # Save the image of the page in system
    page.save(filename, 'JPEG')
    
    # Increment the counter to update filename
    image_counter = image_counter + 1

print('pdf to image conversion done!')

# Start recognizing text in images
file_limit = image_counter

outfile = "text.txt"

# Open the file in append mode 
f = open(outfile, 'a')

# Iterate from 1 to total number of pages
for i in range(1, file_limit):
    filename = "page_" + str(i) + '.jpg'
    
    text = str(((pytesseract.image_to_string(Image.open(filename)))))
    
    text = text.replace('-\n', '')
    
    f.write(text)

f.close()

print('Compelted!')