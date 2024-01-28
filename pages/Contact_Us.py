import streamlit as st

from send_email import send_gmail
from send_email2 import send_from_outlook

st.title("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address:")
    user_message = st.text_area("Your message:")
    message = f"""\
Subject: {user_email}

From: {user_email}
{user_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        print("Submitted!")
        send_from_outlook(message)
