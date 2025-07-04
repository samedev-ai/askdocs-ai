from haystack.document_stores import FAISSDocumentStore

document_store = FAISSDocumentStore(
    faiss_index_factory_str="Flat",  # Using "Flat" index for simplicity
    embedding_dim=768,  # Match embedding model size
    sql_url="sqlite:///faiss_doc_store.db"
)
