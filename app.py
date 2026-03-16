import streamlit as st
from index_pipeline import load_documents, create_index, get_query_engine

# Add App Title
st.title("LlamaIndex Knowledge Base Chatbot")
st.write("Ask questions from your documents")

# Load Documents and Create Index
documents = load_documents()
index = create_index(documents)
query_engine = get_query_engine(index)

# Create Input Box
user_question = st.text_input("Enter your question:")

# Query the Knowledge Base
if user_question:
    response = query_engine.query(user_question)

    st.subheader("Answer")
    st.write(response.response)