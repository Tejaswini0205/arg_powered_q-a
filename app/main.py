import streamlit as st

st.title('RAG-Powered Q&A Assistant')

query = st.text_input('Ask a question')

if query:
    st.write(f'You asked: {query}')
    # Call agent here for response and context retrieval (replace with actual logic later)
    st.write('Response from assistant: [To be implemented]')
    st.write('Context snippets: [To be implemented]')