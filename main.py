# Import langchain dependencies
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import retrieval_qa
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# UI
import streamlit as st

# Watsonx interface
from wxai_langchain.llm import LangChainInterface

# Setup the app title
st.title("Ask XmasBot")

# Setup a session state message variable to store the chat messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display the chat messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['message'])

# Build a prompt input template to display the prompts
prompt = st.chat_input("Type your question here...")

# If enter is pressed
if prompt:
    # Display the prompt
    st.chat_message('user').markdown(prompt)
    # Append the prompt to the messages
    st.session_state.messages.append({'role': 'user', 'message': prompt})
    