from upload import save_uploaded_file
from extract_text import save_uploaded_file,extract_text_from_pdf
from embed_documents import index_document
from qa_pipeline import ask_question

def main():
    # 1. Upload the file
    file_path = save_uploaded_file("uploaded_docs/document.pdf")

    # 2. Extract text from PDF
    extracted_text = extract_text_from_pdf(file_path)

    # 3. Index document (vectorize and store in FAISS or other stores)
    index_document(extracted_text, metadata={"filename": file_path})

    # 4. Ask a question
    question = "What is this document about?"
    result = ask_question(question)
    print(result)

if __name__ == "__main__":
    main()
