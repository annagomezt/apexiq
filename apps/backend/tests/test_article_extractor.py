from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[2]

pdf = (
    ROOT
    / "knowledge_base"
    / "formula1"
    / "sporting"
    / "section_b_sporting.pdf"
)

doc = fitz.open(pdf)

for page_number in range(8, 15):

    print("=" * 80)
    print(f"PAGE {page_number + 1}")
    print("=" * 80)

    page = doc[page_number]

    print(page.get_text()[:4000])