import pdfplumber

with pdfplumber.open(
    "../../knowledge_base/formula2/sporting/sporting_regulations_2026.pdf"
) as pdf:

    print(len(pdf.pages))

    print(pdf.pages[0].extract_text())