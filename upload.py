import os
from pathlib import Path

UPLOAD_DIR = "uploaded_docs"

def save_uploaded_file(uploaded_file):
    # Ensure the uploaded_docs directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Create the file path for the uploaded file
    file_path = Path(UPLOAD_DIR) / Path(uploaded_file.name)

    # Write the content of the uploaded file to the destination
    with open(file_path, "wb") as f_out:
        f_out.write(uploaded_file.getbuffer())  # Streamlit file object has `getbuffer` method

    return file_path
