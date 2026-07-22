# Issue #001 — Formula 2 Sporting Regulations PDF

## Status

🟡 Under Investigation

---

## Description

During the ingestion pipeline development, the official Formula 2 Sporting Regulations (2026) PDF could be opened successfully, but no extractable text was found.

The document contains 58 pages and is recognized by both PyMuPDF and pdfplumber.

However, both libraries fail to extract any textual content.

---

## Observed Behaviour

### PyMuPDF

- PDF opens successfully.
- Page count is correct.
- `page.get_text()` returns an empty string.
- MuPDF emits the following warning:

```
zlib error: incorrect header check
```

---

### pdfplumber

- PDF opens successfully.
- Correct number of pages.
- `extract_text()` returns `None`.

---

## Impact

Currently, this document cannot be indexed by the ingestion pipeline.

Other FIA documents (Formula 1 General, Sporting, Technical, Operational and Formula 2 Technical) are processed successfully.

---

## Possible Causes

- Non-standard compression.
- Corrupted content stream.
- Missing or incompatible text layer.
- Different PDF generation process.

---

## Future Improvements

The ingestion pipeline will support multiple extraction strategies:

- PyMuPDF
- pdfplumber
- OCR (Tesseract)

This architecture will maximize compatibility with heterogeneous FIA documents.

---

## Priority

Low

The issue does not block the development of the remaining pipeline.