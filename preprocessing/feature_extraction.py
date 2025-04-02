import re

def extract_features(text):
    """Extract key features from text such as dates, amounts, and keywords."""
    dates = re.findall(r'\d{2,4}[/-]\d{2}[/-]\d{2,4}', text)
    amounts = re.findall(r'\$?\d{1,3}(?:,\d{3})*(?:\.\d{2})?', text)
    keywords = re.findall(r'(?i)(invoice|contract|report|signature|total)', text)

    return {
        "dates": dates,
        "amounts": amounts,
        "keywords": keywords
    }
