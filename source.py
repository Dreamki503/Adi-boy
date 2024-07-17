import streamlit as st
from groq import Groq

st.set_page_config(page_title="Adi",page_icon="Adi.jpg")
st.image("Adi.jpg",width=100)
st.title("Welcome to :red[Adi boy]")
st.divider()

# OpenAI initialize
client = Groq(api_key = st.secrets["api_key"])

if "model" not in st.session_state:
    st.session_state["model"] = "llama3-70b-8192"

def draft_message(content ,role = "user"):
    return {
        "content" : content,
        "role" : role
    }

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

#Add initial system message but do not print it 
if "system_nessage_added" not in st.session_state:
    st.session_state.messages.append(
        {
            "role" : "system",
            "content" : "Your name is Adi. You are 21 years old.You are slightly dumb but you talk like a regular guy. You are a grandmaster at chess. You like milfs.You only talk about chess and milfs when someone asks you."
        }
    )
    st.session_state.system_message_added = True

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# React to user input
prompt = st.chat_input("What's up")
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append(draft_message(prompt))

    with st.chat_message("assistant",avatar = "Adi.jpg"):
        message_placeholder = st.empty()
        full_response = ""

        # Collect messages for the conversation
        conversation = st.session_state.messages.copy()
        conversation.append(draft_message(prompt))

        response = client.chat.completions.create(temperature = 1,
            model= st.session_state["model"],
            max_tokens= 1000,
            messages= conversation)
        
        response.usage.total_tokens

        content = response.choices[0].message.content
        full_response += content
        message_placeholder.markdown(full_response + "|")

        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
