import streamlit as st
from upload import save_uploaded_file
from extract_text import extract_text_from_pdf
from embed_documents import index_document
from qa_pipeline import ask_question
from config import setup_openai_api
import pyperclip

def main():
    st.title("📚 Document Upload and QA System")
    st.markdown("---")
    
    # Setup OpenAI API
    if not setup_openai_api():
        st.stop()
    
    # Initialize session state for managing answers
    if 'current_answer' not in st.session_state:
        st.session_state.current_answer = None
    if 'current_question' not in st.session_state:
        st.session_state.current_question = ""
    
    # 1. Allow user to upload a file via Streamlit's file uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # 2. Save the uploaded file
        file_path = save_uploaded_file(uploaded_file)
        
        with st.spinner("Processing document..."):
            # 3. Extract text from the PDF file
            extracted_text = extract_text_from_pdf(file_path)
            
            # 4. Index the document (vectorize and store)
            index_document(extracted_text, metadata={"filename": uploaded_file.name})
        
        st.success(f"✅ Document '{uploaded_file.name}' processed successfully!")
        
        # 5. Ask a question - Better horizontal layout
        st.markdown("### 🤔 Ask Questions About Your Document")
        
        # Create a form for better layout control
        with st.form("question_form"):
            col1, col2 = st.columns([4, 1])
            with col1:
                question = st.text_input("Ask a question:", placeholder="e.g., Summarize this document", key="question_input")
            with col2:
                ask_button = st.form_submit_button("🚀 Ask", use_container_width=True)
            
            if ask_button and question:
                with st.spinner("Generating answer..."):
                    answer = ask_question(question)
                    st.session_state.current_answer = answer
                    st.session_state.current_question = question
                st.rerun()
        
        # Display the answer if available
        if st.session_state.current_answer:
            st.markdown("---")
            st.markdown(f"### 💡 Answer for: *{st.session_state.current_question}*")
            
            # Answer in a styled container (dark-friendly)
            with st.container():
                formatted_answer = st.session_state.current_answer.replace('\n', '<br>')
                st.markdown(
                    f"""
                    <div style='background-color: rgba(30,30,30,0.95); color: #fff; border-radius: 10px; padding: 20px; border-left: 4px solid #007bff; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); font-size: 1.1em;'>
                        {formatted_answer}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                # Copy button in a horizontal layout
                col1, col2, col3 = st.columns([1, 1, 3])
                with col1:
                    if st.button("📋 Copy Answer", key="copy_main"):
                        pyperclip.copy(st.session_state.current_answer)
                        st.success("Copied to clipboard!")
                with col2:
                    if st.button("🗑️ Clear", key="clear_main"):
                        st.session_state.current_answer = None
                        st.session_state.current_question = ""
                        st.rerun()
        
        # Example questions section
        st.markdown("---")
        st.markdown("### 💡 Quick Questions")
        st.markdown("Click any example question below:")
        
        # Example questions in a grid layout
        example_questions = [
            "Summarize this document",
            "What are the main points?",
            "What is this document about?",
            "What are the key findings?"
        ]
        
        # Create 2x2 grid for example questions
        cols = st.columns(2)
        for i, example in enumerate(example_questions):
            with cols[i % 2]:
                if st.button(example, key=f"example_{i}", use_container_width=True):
                    with st.spinner("Generating answer..."):
                        answer = ask_question(example)
                        st.session_state.current_answer = answer
                        st.session_state.current_question = example
                    st.rerun()
    
    else:
        st.info("📄 Please upload a PDF file to get started.")
        st.markdown("""
        ### How it works:
        1. **Upload** a PDF document
        2. **Process** - The system extracts text and creates embeddings
        3. **Ask** questions about the document
        4. **Get** AI-powered answers using GPT models
        
        ### Features:
        - ✅ **Smart Summarization** - Get 2-3 paragraph summaries
        - ✅ **Semantic Search** - Find relevant information quickly
        - ✅ **Natural Language** - Ask questions in plain English
        - ✅ **Context-Aware** - Answers based on your document content
        """)
    
if __name__ == "__main__":
    main()
