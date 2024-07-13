import streamlit as st
from groq import Groq

st.title(":red[ADI BOY]")
st.text("I am Adi and i am dumb")
st.divider()

client = Groq(api_key= "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" )
def draft_message(content ,role = "user"):
    return {
        "content" : content,
        "role" : role
    }


message = [
    {
        "role" : "system",
        "content" : "Your name is Adi. You are dumb but you talk like a regular guy. You are a grandmaster at chess. You like milfs"
    }
]

prompt = st.chat_input("Enter something")
if prompt != None:
    st.write(prompt)

message.append(draft_message(prompt))

if prompt != None:
    response = client.chat.completions.create(
        temperature = 1,
        model= "llama3-70b-8192",
        max_tokens= 1000,
        messages= message
    )

    response.usage.total_tokens
    st.write(response.choices[0].message.content)
