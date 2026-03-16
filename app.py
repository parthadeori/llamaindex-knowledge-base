import streamlit as st
from index_pipeline import load_documents, create_index, get_query_engine

# Add App Title
st.title("LlamaIndex Knowledge Base Chatbot")
st.write("Ask questions from your documents")

# Add Cache Function
@st.cache_resource
def load_index():
    documents = load_documents()
    index = create_index(documents)
    query_engine = get_query_engine(index)
    return query_engine

# Use Cached Index
query_engine = load_index()

# Add Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create Chat Input
prompt = st.chat_input("Ask a question about your documents")

# Handle User Message
if prompt:
    st.session_state.messages.append(
        {
            "role": "user", 
            "content": prompt
         }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = query_engine.query(prompt)
    answer = response.response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)