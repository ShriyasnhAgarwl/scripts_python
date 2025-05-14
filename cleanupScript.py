# Remove all Unicode characters and replace them with plain ASCII equivalents

# Fixing en-dash and other special characters
itinerary_text_clean = itinerary_text_ascii.replace("–", "-").replace("’", "'")

# Re-create PDF with only ASCII characters
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.multi_cell(0, 10, itinerary_title_ascii, align='C')
pdf.ln(5)
pdf.set_font("Arial", '', 11)
pdf.multi_cell(0, 8, itinerary_text_clean)

# Save cleaned PDF
pdf_path = "/mnt/data/Kedarnath_Badrinath_Itinerary.pdf"
pdf.output(pdf_path)

pdf_path
