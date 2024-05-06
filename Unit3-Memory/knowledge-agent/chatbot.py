import streamlit as st
from KnowledgeAgent import Memory, Chatbot

st.title("Gift Recommendation agent")

##Initialize the Agents:
memory_agent = Memory(model='meta-llama/Llama-3-8b-chat-hf', temperature=0.2)
rec_agent = Chatbot(model='gpt-4-turbo-preview', temperature=0.3)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type your question here."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant response in chat message container
    ### Add to memory
    mem_result = memory_agent.run(prompt)
    st.write("Memory agent output: ", mem_result['text'])
    ## Get response
    response = rec_agent.run(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
