from PIL import Image, ImageOps
from pytesseract import pytesseract
  
# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Example: path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


image_path = "text.png"
# Example: image_path = r"C:\Users\Dell\Desktop\text.png"


# Opening the image & storing it in an image object
img = Image.open(image_path).convert("LA")

# multiply each pixel by 1.2
img = img.point(lambda i: i * 1.3)

# enh = ImageEnhance.Contrast(out)
# enh.enhance(1.3).show("30% more contrast")

pixels = img.getdata()

newPixels = []
# Compare each pixel 
for pixel in pixels:
    if pixel < threshold:
        newPixels.append(black)
    else:
        newPixels.append(white)

# Create and save new image.
img = Image.new("RGB",img.size)
img.putdata(newPixels)
img.save("result.jpg")


# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])
