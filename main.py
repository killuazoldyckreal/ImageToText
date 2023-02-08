from PIL import Image, ImageOps
from pytesseract import pytesseract
  
# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Example: path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


image_path = "text.png"
# Example: image_path = r"C:\Users\Dell\Desktop\text.png"


# Opening the image & storing it in an image object
img = Image.open(image_path).convert("L")
gray = ImageOps.grayscale(img)

# Increase the contrast of the image
contrast = ImageOps.autocontrast(gray, cutoff=0)
img = ImageOps.autocontrast(img)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])
