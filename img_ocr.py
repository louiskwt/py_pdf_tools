from PIL import Image
import pytesseract

# Set up output
output = 'output.txt'
f = open(output, 'a')

# Load the img
filename = 'test.jpeg'

text = str(((pytesseract.image_to_string(Image.open(filename)))))

text = text.replace('-\n', '')

f.write(text)

f.close()

print('Completed')
    
    
    