# AI System for Automated Document Analysis and Classification (Without LLMs)

## Project Overview

This project aims to develop a local AI-powered system capable of:

- Extracting text from scanned or digital documents.
- Classifying documents into predefined categories (e.g., invoices, contracts, reports).
- Detecting anomalies such as missing signatures, unusual amounts, or missing fields.
- Visualizing insights from analyzed documents.

## Features

- **OCR Processing**: Extracts text from PDFs and images using Tesseract OCR and OpenCV.
- **Feature Extraction**: Identifies key elements such as dates, monetary amounts, and keywords.
- **Document Classification**: Uses machine learning models to categorize documents.
- **Anomaly Detection**: Flags missing information and unusual patterns.
- **Dashboard (Upcoming)**: A web-based interface to display document insights.

## Project Structure

```
document_analysis_project/
│── data/                 # Sample documents (PDFs, images)
│── models/               # Trained ML models
│── preprocessing/        # OCR, text extraction, cleaning
│── feature_extraction/   # Extract text, metadata
│── classification/       # Document classification model
│── anomaly_detection/    # Rule-based & ML-based anomaly detection
│── ui/                   # Streamlit/Flask visualization
│── main.py               # Main entry point
│── requirements.txt      # Dependencies
│── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mirouhlar/document_analysis_project.git
   cd document_analysis_project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main script:
   ```bash
   python main.py
   ```

## Future Goals

- Improve document classification accuracy with additional training data.
- Implement a rule-based and ML-based anomaly detection model.
- Develop a user-friendly web interface using Streamlit or Flask.
- Optimize OCR preprocessing for better accuracy.
- Support more document types and languages.

## License

This project is open-source under the MIT License.

---

For any issues, feel free to open a GitHub issue or reach out.
