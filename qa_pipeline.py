from embed_documents import search_documents
import openai
import os

# Set up OpenAI API key
# You'll need to set your API key as an environment variable or in a .env file
# os.environ["OPENAI_API_KEY"] = "your-api-key-here"

def ask_question(query, top_k=5):
    """Ask a question and get an answer based on the most relevant documents using OpenRouter models"""
    # Search for relevant documents
    search_results = search_documents(query, top_k=top_k)
    
    if not search_results:
        return "No relevant documents found to answer your question."
    
    # Combine the most relevant documents into context
    context = " ".join([result['document'].content for result in search_results])
    
    # Determine if this is a summarization request
    summarization_keywords = ['summarize', 'summary', 'summarise', 'overview', 'brief', 'main points']
    is_summarization = any(keyword in query.lower() for keyword in summarization_keywords)
    
    if is_summarization:
        more_results = search_documents(query, top_k=10)
        full_context = " ".join([result['document'].content for result in more_results])
        system_prompt = (
            "You are a helpful assistant that creates comprehensive summaries. "
            "Provide detailed summaries in 2-3 paragraphs covering the main points, key information, and important details from the provided document."
        )
        user_prompt = f"""Please provide a comprehensive summary of the following document in 2-3 paragraphs:\n\nDocument content:\n{full_context}\n\nSummary:"""
        # Use Llama 2 for better summarization (correct OpenRouter model name)
        model = "meta/llama-2-70b-chat"
        max_tokens = 800
    else:
        system_prompt = (
            "You are a helpful assistant that answers questions based on the provided document context. "
            "Provide accurate, detailed answers using only the information from the document."
        )
        user_prompt = f"""Based on the following document context, please answer this question: {query}\n\nDocument context:\n{context}\n\nAnswer:"""
        # Use Mistral for regular questions (faster and cheaper) - correct OpenRouter model name
        model = "mistralai/mistral-7b-instruct"
        max_tokens = 500
    
    try:
        # Configure OpenAI client to use OpenRouter
        client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.3,
            top_p=0.9
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating response: {str(e)}. Please check your OpenRouter API key and internet connection."
