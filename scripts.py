import os
from preprocessing.ocr_processing import extract_text, extract_text_from_pdf
from feature_extraction.feature_extraction import extract_features

def process_document(file_path):

    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text(file_path)
    
    features = extract_features(text)
    return text, features

if __name__ == "__main__":
    sample_pdf = "data/sample2.pdf"
    sample_image = "data/sample.png"
    
    if os.path.exists(sample_pdf):
        text, features = process_document(sample_pdf)
    elif os.path.exists(sample_image):
        text, features = process_document(sample_image)
    else:
        print("No sample document found.")
        exit()
    
    print("Extracted Text:\n", text)
    print("Extracted Features:\n", features)
