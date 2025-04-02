from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_sample_pdf(output_path="data/sample.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(100, 750, "Invoice #12345")
    c.drawString(100, 730, "Date: 2024-04-02")
    c.drawString(100, 710, "Company: ABC Corp")
    c.drawString(100, 690, "Total Amount: $1,250.00")
    c.drawString(100, 670, "Signature: ____________________")

    c.save()
    print(f"Sample PDF saved at: {output_path}")

if __name__ == "__main__":
    create_sample_pdf()
