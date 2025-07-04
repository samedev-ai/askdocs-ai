import os
import fitz  # PyMuPDF
from pathlib import Path

UPLOAD_DIR = "uploaded_docs"

def save_uploaded_file(file_path):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    dest = Path(UPLOAD_DIR) / Path(file_path).name
    if dest.exists():
        print("File already exists, skipping upload.")
        return dest
    with open(file_path, "rb") as f_in, open(dest, "wb") as f_out:
        f_out.write(f_in.read())
    return dest

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

