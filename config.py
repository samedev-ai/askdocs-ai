import os
import streamlit as st

def setup_openai_api():
    """Setup OpenRouter API key from environment or Streamlit secrets"""
    
    # Try to get API key from environment variable
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    # If not in environment, try to get from Streamlit secrets
    if not api_key:
        try:
            api_key = st.secrets["OPENROUTER_API_KEY"]
        except:
            pass
    
    # If still not found, show a warning
    if not api_key:
        st.warning("⚠️ OpenRouter API key not found! Please set it up.")
        st.info("You can set your API key in one of these ways:")
        st.markdown("""
        1. **Environment Variable**: Set `OPENROUTER_API_KEY=your-key-here`
        2. **Streamlit Secrets**: Create `.streamlit/secrets.toml` with:
           ```toml
           OPENROUTER_API_KEY = "your-key-here"
           ```
        3. **Direct Input**: Enter it below (not recommended for production)
        """)
        
        # Allow manual input (for testing only)
        api_key = st.text_input("Enter your OpenRouter API key (optional):", type="password")
    
    if api_key:
        os.environ["OPENROUTER_API_KEY"] = api_key
        return True
    
    return False 