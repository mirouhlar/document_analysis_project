import os
import cv2
import pytesseract
from pdf2image import convert_from_path

os.environ["TESSDATA_PREFIX"] = "/opt/local/share/tessdata/"


def preprocess_image(image_path):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return image

def extract_text(image_path):

    processed_image = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_image)
    return text

def extract_text_from_pdf(pdf_path):

    pages = convert_from_path(pdf_path)
    extracted_text = ""
    for page in pages:
        temp_path = "temp_page.png"
        page.save(temp_path, 'PNG')
        extracted_text += extract_text(temp_path) + "\n"
        os.remove(temp_path)
    return extracted_text
