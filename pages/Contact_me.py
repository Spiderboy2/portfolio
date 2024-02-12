import streamlit as st
from email_bg import send_mail

st.header("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email")
    form_message = st.text_area("enter your message")
    message = f"""\
Subject: messege from {user_email}

{form_message}
from : {user_email}

"""

    button = st.form_submit_button("submit")
    print(button)
    if button:
        send_mail(message)
        st.info("your message was sent sucessfully")


