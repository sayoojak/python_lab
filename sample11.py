import streamlit as st
 
st.title("Login Form")
username = st.text_input("Enter username")
password = st.text_input("Enter password", type="password")
 
if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("Login successful!")
    else:
        st.error("Invalid username or password")
