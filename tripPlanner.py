# Re-creating the PDF using only ASCII characters to avoid encoding issues

# Replacing emojis with plain text equivalents for compatibility
itinerary_title_ascii = "Kedarnath + Badrinath Yatra Itinerary (Fastest Possible with Minimum Leave)"

itinerary_text_ascii = """
Duration: 5 Days (Weekend + 2 Leaves)
Style: On Foot (Kedarnath Trek) + Road (Badrinath)
Route: Delhi -> Haridwar -> Kedarnath -> Badrinath -> Delhi
Ideal Time: May–June or September–October

Day 0 (Evening): Delhi -> Haridwar/Rishikesh
- Leave by overnight Volvo or train (8–9 PM)
- Reach Haridwar/Rishikesh early morning (3–4 AM)

Day 1: Haridwar -> Sonprayag -> Gaurikund
- Start early from Haridwar (4–5 AM) via shared jeep/private cab
- Reach Sonprayag (8–10 hrs), complete biometric registration
- Continue to Gaurikund (last motorable point), stay overnight

Day 2: Gaurikund -> Kedarnath (16 km trek)
- Start trek at 4–5 AM, reach Kedarnath by noon/afternoon
- Darshan and overnight stay at Kedarnath (book GMVN or tents)

Day 3: Kedarnath -> Gaurikund -> Badrinath
- Early trek down to Gaurikund (4–6 hrs)
- Drive to Badrinath via Joshimath (approx. 8–10 hrs)
- Reach Badrinath by evening/night, stay overnight

Day 4: Badrinath Darshan -> Return Journey
- Visit Badrinath Temple early morning
- Begin return journey via Joshimath -> Rudraprayag -> Rishikesh
- Board overnight bus/train to Delhi

Day 5 (Optional): Arrival in Delhi
- Reach Delhi early morning (4–6 AM), go to work if needed

Trek & Travel Summary:
- Kedarnath Trek: 16 km one way (on foot)
- Badrinath: Accessible by road
- Total Distance (Road): Approx. 1100 km round trip

Leaves Required: 2 Days (Fri & Mon or Mon & Tue)
Budget: Rs. 6000–9000 (includes travel, stay, food)
"""

# Create PDF again
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.multi_cell(0, 10, itinerary_title_ascii, align='C')
pdf.ln(5)
pdf.set_font("Arial", '', 11)
pdf.multi_cell(0, 8, itinerary_text_ascii)

# Save new PDF
pdf_path = "/mnt/data/Kedarnath_Badrinath_Itinerary.pdf"
pdf.output(pdf_path)

pdf_path
