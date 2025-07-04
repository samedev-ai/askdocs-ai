from haystack import Document
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle
import os

# Initialize the embedding model
embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Simple in-memory storage for documents and embeddings
documents = []
embeddings = []

def index_document(text, metadata=None):
    """Index a document by splitting into paragraphs and computing embeddings"""
    global documents, embeddings
    
    # Split text into paragraphs
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    
    # Create documents
    docs = []
    for i, paragraph in enumerate(paragraphs):
        doc_meta = metadata.copy() if metadata else {}
        doc_meta['paragraph_id'] = i
        doc = Document(content=paragraph, meta=doc_meta)
        docs.append(doc)
    
    # Compute embeddings
    texts = [doc.content for doc in docs]
    paragraph_embeddings = embedding_model.encode(texts)
    
    # Store documents and embeddings
    documents.extend(docs)
    embeddings.extend(paragraph_embeddings)
    
    # Save to disk for persistence
    save_to_disk()
    
    print(f"Indexed {len(docs)} paragraphs from document")

def save_to_disk():
    """Save documents and embeddings to disk"""
    data = {
        'documents': documents,
        'embeddings': embeddings
    }
    with open('document_store.pkl', 'wb') as f:
        pickle.dump(data, f)

def load_from_disk():
    """Load documents and embeddings from disk"""
    global documents, embeddings
    if os.path.exists('document_store.pkl'):
        with open('document_store.pkl', 'rb') as f:
            data = pickle.load(f)
            documents = data['documents']
            embeddings = data['embeddings']

def search_documents(query, top_k=3):
    """Search for similar documents using cosine similarity"""
    if not documents:
        load_from_disk()
    
    if not documents:
        return []
    
    # Compute query embedding
    query_embedding = embedding_model.encode([query])
    
    # Compute similarities
    similarities = []
    for emb in embeddings:
        similarity = np.dot(query_embedding[0], emb) / (np.linalg.norm(query_embedding[0]) * np.linalg.norm(emb))
        similarities.append(similarity)
    
    # Get top-k results
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    
    results = []
    for idx in top_indices:
        results.append({
            'document': documents[idx],
            'similarity': similarities[idx]
        })
    
    return results

# Load existing documents on import
load_from_disk()
