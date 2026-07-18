from langchain_core.messages import HumanMessage
import streamlit as st
from backend import chatbot

CONFIG = {'configurable':{"thread_id":"1"}}

if 'log' not in st.session_state: 
    st.session_state['log'] = []

# Print chat history 
for message in st.session_state['log']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input("Type here")

if user_input:
    st.session_state['log'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # response = chatbot.invoke({'message':HumanMessage(content=user_input)},config = CONFIG)
    # ai_message = response['message'][-1].text
    # with st.chat_message('assistant'):
    #    st.text(ai_message)

    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            message_chunk.text for message_chunk, metadata in chatbot.stream(
              {'message':[HumanMessage(content=user_input)]},
              config = {'configurable':{"thread_id":"1"}},
              stream_mode = "messages",
              flush=True
            )
        )
    st.session_state['log'].append({'role':'assistant','content':ai_message})
        

