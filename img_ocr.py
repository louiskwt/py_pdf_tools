from PIL import Image
import pytesseract

# Set up output file
output = 'output.txt'
f = open(output, 'a')

# Load the img
filename = 'test.jpeg'

# extract the text from image
text = str(((pytesseract.image_to_string(Image.open(filename)))))

text = text.replace('-\n', '')

# write to output file
f.write(text)

f.close()

print('Completed')
    
    
    