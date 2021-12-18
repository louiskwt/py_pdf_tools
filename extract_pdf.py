import pdftotext

# Load your PDF
with open("example.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)


# How many pages?
print(len(pdf))

# Iterate over all the pages
for page in pdf:
    print(page)

