<<<<<<< HEAD
# 📚 Document Upload and QA System

> **An AI-powered document analysis system that extracts insights from your PDF documents using advanced language models.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red.svg)](https://streamlit.io)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-API-green.svg)](https://openrouter.ai)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Quick Start

<details>
<summary><strong>🎯 Click to expand Quick Start Guide</strong></summary>

### 1. Clone & Setup
```bash
git clone <your-repo-url>
cd python
pip install -r requirements.txt
```

### 2. Set up API Key
Choose one of these methods:

**Option A: Environment Variable**
```bash
export OPENROUTER_API_KEY="your-api-key-here"
```

**Option B: Streamlit Secrets (Recommended)**
```bash
mkdir .streamlit
echo 'OPENROUTER_API_KEY = "your-api-key-here"' > .streamlit/secrets.toml
```

### 3. Run the Application
```bash
streamlit run app.py
```

### 4. Open in Browser
Navigate to `http://localhost:8501` and start uploading documents!

</details>

## ✨ Features

<details>
<summary><strong>🔥 Core Features</strong></summary>

- **📄 PDF Upload & Processing** - Drag and drop any PDF document
- **🧠 AI-Powered Q&A** - Ask questions in natural language
- **🔍 Semantic Search** - Find relevant information using embeddings
- **📋 Smart Summarization** - Get comprehensive document summaries
- **💾 Persistent Storage** - Documents are indexed and stored locally
- **🎨 Interactive UI** - Clean, user-friendly Streamlit interface
- **📱 Responsive Design** - Works on desktop and mobile

</details>

<details>
<summary><strong>🤖 AI Models Used</strong></summary>

- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Question Answering**: `mistralai/mistral-7b-instruct`
- **Summarization**: `meta/llama-2-70b-chat`

</details>

## 🏗️ Project Structure

<details>
<summary><strong>📁 Click to view project structure</strong></summary>

```
python/
├── 📱 app.py              # Main Streamlit application
├── 🔧 main.py             # Command-line interface
├── ⚙️ config.py           # API configuration
├── 📋 requirements.txt    # Dependencies
├── 
├── 📂 Core Modules:
│   ├── 📤 upload.py       # File upload handling
│   ├── 📖 extract_text.py # PDF text extraction
│   ├── 🧠 embed_documents.py # Document embedding & search
│   └── 💬 qa_pipeline.py  # Question answering pipeline
├── 
├── 📂 Storage:
│   ├── 📁 uploaded_docs/  # Uploaded PDF files
│   └── 💾 document_store.pkl # Indexed documents & embeddings
└── 
└── 📂 Cache:
    └── 🗂️ __pycache__/     # Python cache files
```

</details>

## 🎯 How It Works

<details>
<summary><strong>🔄 Click to understand the workflow</strong></summary>

### Step-by-Step Process:

1. **📤 Upload**: User uploads a PDF document through the web interface
2. **🔍 Extract**: System extracts text from the PDF using PyMuPDF
3. **✂️ Chunk**: Text is split into meaningful paragraphs
4. **🧠 Embed**: Each paragraph is converted to vector embeddings
5. **💾 Store**: Documents and embeddings are stored locally
6. **❓ Query**: User asks a question about the document
7. **🔍 Search**: System finds most relevant paragraphs using similarity search
8. **🤖 Generate**: AI model generates an answer based on relevant context
9. **📋 Display**: Answer is presented with copy/clear options

</details>

## 🛠️ Installation & Setup

<details>
<summary><strong>🔧 Detailed Installation Guide</strong></summary>

### Prerequisites
- Python 3.8 or higher
- pip package manager
- OpenRouter API key ([Get one here](https://openrouter.ai))

### Step 1: Environment Setup
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: API Configuration
Create your API key configuration:

**Method 1: Environment Variable**
```bash
# Windows
set OPENROUTER_API_KEY=your-api-key-here

# macOS/Linux
export OPENROUTER_API_KEY=your-api-key-here
```

**Method 2: Streamlit Secrets (Recommended for deployment)**
```bash
mkdir .streamlit
cat > .streamlit/secrets.toml << EOF
OPENROUTER_API_KEY = "your-api-key-here"
EOF
```

### Step 4: Test Installation
```bash
# Test with command line interface
python main.py

# Or run the web app
streamlit run app.py
```

</details>

## 📖 Usage Examples

<details>
<summary><strong>💡 Example Questions & Use Cases</strong></summary>

### 📊 Document Analysis
```
• "Summarize this document"
• "What are the main points?"
• "What is this document about?"
• "What are the key findings?"
```

### 🔍 Specific Information
```
• "What are the conclusions?"
• "Are there any recommendations?"
• "What methodology was used?"
• "What are the limitations mentioned?"
```

### 📈 Data Extraction
```
• "What statistics are mentioned?"
• "Are there any dates or deadlines?"
• "What companies are mentioned?"
• "What are the financial figures?"
```

### 🎯 Research Questions
```
• "What evidence supports the main argument?"
• "What are the counterarguments?"
• "What future research is suggested?"
• "What are the practical implications?"
```

</details>

## 🔧 Configuration

<details>
<summary><strong>⚙️ Advanced Configuration Options</strong></summary>

### Model Configuration
You can modify the models used in `qa_pipeline.py`:

```python
# For regular questions (faster, cheaper)
model = "mistralai/mistral-7b-instruct"

# For summarization (better quality)
model = "meta/llama-2-70b-chat"

# Alternative models you can try:
# "anthropic/claude-3-haiku"
# "openai/gpt-3.5-turbo"
# "google/gemini-pro"
```

### Search Configuration
Adjust search parameters in `embed_documents.py`:

```python
# Number of similar paragraphs to retrieve
top_k = 3  # Default for questions
top_k = 10  # Default for summarization

# Embedding model (can be changed)
embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
```

### Upload Configuration
Modify upload settings in `upload.py`:

```python
UPLOAD_DIR = "uploaded_docs"  # Change upload directory
# Add file size limits, allowed types, etc.
```

</details>

## 🐛 Troubleshooting

<details>
<summary><strong>🔍 Common Issues & Solutions</strong></summary>

### ❌ API Key Issues
```bash
# Problem: "API key not found"
# Solution: Verify your API key is set correctly
echo $OPENROUTER_API_KEY  # Should show your key
```

### ❌ Module Import Errors
```bash
# Problem: "ModuleNotFoundError"
# Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### ❌ PDF Processing Issues
```bash
# Problem: "Cannot extract text from PDF"
# Solution: Check if PDF is text-based (not scanned image)
# For scanned PDFs, you'd need OCR functionality
```

### ❌ Memory Issues
```bash
# Problem: "Out of memory"
# Solution: Process smaller documents or increase system memory
# Consider chunking large documents differently
```

### ❌ Streamlit Issues
```bash
# Problem: "Port already in use"
# Solution: Run on different port
streamlit run app.py --server.port 8502
```

</details>

## 🚀 Advanced Usage

<details>
<summary><strong>🔬 Advanced Features & Customization</strong></summary>

### Command Line Interface
For batch processing or automation:

```bash
# Process a document programmatically
python main.py
```

### Custom Embedding Models
You can experiment with different embedding models:

```python
# In embed_documents.py, try:
# 'sentence-transformers/all-mpnet-base-v2'  # Better quality
# 'sentence-transformers/all-MiniLM-L12-v2'  # Balanced
# 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'  # Multilingual
```

### Adding New Document Types
Extend the system to support other formats:

```python
# Add to extract_text.py
def extract_text_from_docx(file_path):
    # Implementation for Word documents
    pass

def extract_text_from_txt(file_path):
    # Implementation for text files
    pass
```

### Custom Prompts
Modify the AI prompts in `qa_pipeline.py`:

```python
# Customize system prompts for different use cases
system_prompt = "You are a legal document analyst..."  # For legal docs
system_prompt = "You are a research paper reviewer..."  # For academic papers
```

</details>

## 📊 Performance & Scalability

<details>
<summary><strong>⚡ Performance Optimization Tips</strong></summary>

### 🚀 Speed Optimizations
- **Embedding Caching**: Embeddings are cached locally in `document_store.pkl`
- **Model Selection**: Choose faster models for real-time interactions
- **Batch Processing**: Process multiple documents at once

### 📈 Scaling Considerations
- **Vector Databases**: Consider FAISS, Pinecone, or Weaviate for large datasets
- **Cloud Deployment**: Deploy on AWS, GCP, or Azure for scalability
- **Load Balancing**: Use multiple instances for high traffic

### 💾 Storage Management
- **Cleanup**: Regularly clean up old documents and embeddings
- **Compression**: Use document compression for large files
- **Database**: Consider PostgreSQL with pgvector for production

</details>

## 🤝 Contributing

<details>
<summary><strong>🎉 How to Contribute</strong></summary>

We welcome contributions! Here's how you can help:

### 🐛 Bug Reports
- Use the issue tracker to report bugs
- Include steps to reproduce
- Provide system information

### 💡 Feature Requests
- Suggest new features or improvements
- Explain the use case and benefit
- Consider implementation complexity

### 🔧 Code Contributions
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### 📝 Documentation
- Improve README sections
- Add code comments
- Create tutorials or examples

</details>

## 📄 License

<details>
<summary><strong>📜 MIT License</strong></summary>

```
MIT License

Copyright (c) 2024 Document QA System

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

</details>

## 🔗 Links & Resources

<details>
<summary><strong>📚 Useful Resources</strong></summary>

### 🛠️ Technologies Used
- **[Streamlit](https://streamlit.io)** - Web app framework
- **[OpenRouter](https://openrouter.ai)** - AI model API
- **[Sentence Transformers](https://www.sbert.net)** - Embedding models
- **[PyMuPDF](https://pymupdf.readthedocs.io)** - PDF processing
- **[Haystack](https://haystack.deepset.ai)** - NLP framework

### 📖 Documentation
- [Streamlit Documentation](https://docs.streamlit.io)
- [OpenRouter Models](https://openrouter.ai/docs)
- [Sentence Transformers Models](https://www.sbert.net/docs/pretrained_models.html)

### 🎓 Learning Resources
- [Building RAG Systems](https://www.deeplearning.ai/short-courses/building-applications-vector-databases/)
- [Streamlit Tutorials](https://docs.streamlit.io/library/get-started/tutorials)
- [Vector Embeddings Guide](https://www.pinecone.io/learn/vector-embeddings/)

</details>

---

<div align="center">

### 🎉 Ready to analyze your documents with AI?

**[⬆️ Back to Top](#-document-upload-and-qa-system)** | **[🚀 Quick Start](#-quick-start)** | **[📖 Usage Examples](#-usage-examples)**

---

**Made with ❤️ by the Document QA Team**

*If you find this project helpful, please consider giving it a ⭐ star!*

</div>

## 🔍 Interactive Elements

<details>
<summary><strong>🎮 Try These Interactive Commands</strong></summary>

### Quick Test Commands
```bash
# Test your setup
python -c "import streamlit, openai, sentence_transformers; print('✅ All dependencies installed!')"

# Check API key
python -c "import os; print('✅ API key found!' if os.getenv('OPENROUTER_API_KEY') else '❌ API key not found')"

# Launch app
streamlit run app.py --server.headless true --server.port 8501
```

### Sample Questions to Try
Once you upload a document, try these sample questions:

```
📊 "Give me a 2-paragraph summary of this document"
🔍 "What are the three most important points?"
📈 "Are there any statistics or numbers mentioned?"
🎯 "What recommendations does this document make?"
❓ "What questions does this document raise?"
```

</details>

---

*This interactive README was generated to help you get the most out of your Document QA System. Each section is expandable to show detailed information while keeping the main view clean and navigable.*
=======
# askdocs-ai
A Python RAG app to upload documents and get answers via AI
>>>>>>> 78d695f599b162a18fbbe2229019f49f0a378a94
