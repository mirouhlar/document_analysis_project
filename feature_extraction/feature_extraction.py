import re
from dateutil import parser

def extract_dates(text):

    date_patterns = [
        r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",  # MM/DD/YYYY, DD-MM-YYYY
        r"\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b",  # YYYY/MM/DD
        r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}\b",  # Month DD, YYYY
        r"\b\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}\b"  # DD Month YYYY
    ]
    
    found_dates = []
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        found_dates.extend(matches)

    # Convert to standard YYYY-MM-DD format
    normalized_dates = []
    for date_str in found_dates:
        try:
            parsed_date = parser.parse(date_str, dayfirst=True)
            normalized_dates.append(parsed_date.strftime("%Y-%m-%d"))
        except Exception as e:
            print(f"Error parsing date {date_str}: {e}")

    return normalized_dates

def extract_currencies(text):

    currency_patterns = [
        r"(\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)",  # $1,000.50 USD
        r"(€\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?)",  # €1.000,75 EUR
        r"(£\d{1,3}(?:,\d{3})*(?:\.\d{2})?)",  # £500.99 GBP
        r"(₹\d{1,3}(?:,\d{2})*(?:,\d{3})*)",  # ₹1,00,000 INR
        r"(\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s?(USD|EUR|GBP|INR|JPY))"  # 1000 JPY
    ]
    
    found_currencies = []
    for pattern in currency_patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if isinstance(match, tuple):  # Some regex patterns return tuples
                found_currencies.append("".join(match))
            else:
                found_currencies.append(match)

    return found_currencies


# def extract_features(text):

#     dates = re.findall(r'\d{2,4}[/-]\d{2}[/-]\d{2,4}', text)
#     amounts = re.findall(r'\$?\d{1,3}(?:,\d{3})*(?:\.\d{2})?', text)
#     keywords = re.findall(r'(?i)(invoice|contract|report|signature|total)', text)

#     return {
#         "dates": dates,
#         "amounts": amounts,
#         "keywords": keywords
#     }


def extract_features(text):
    features = {
        "dates": extract_dates(text),
        "currencies": extract_currencies(text)
    }
    return features