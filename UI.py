import  streamlit as st
import requests

# st.title("Test title")
st.header("This own chatBox")
st.info("build by souvikD")
# st.error("error text")
# st.write(range(1,100))
# st.write("My name is Khan")
#
# st.checkbox("click me")
# st.button("hey")
def callingBE(input:str):
    url="http://localhost:8000/chat"
    body={
        "message":input
    }
    return requests.post(url,json=body).json()

input=st.text_input("chat input")
if input:
    with st.spinner("Thinking....."):
        res=callingBE(input)
        st.write(res)

