import smtplib
import ssl
import os


def send_from_outlook(message):
    host = "smtp-mail.outlook.com"
    port = 587
    username = os.getenv("username")
    password = os.getenv("password")
    receiver = os.getenv("receiver")
    # message = '''
    # Maanae thaenae kattippudi
    # Maaman thola thottukkadi
    # '''
    # context = ssl.create_default_context()
    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, receiver, message)

# send_from_outlook()
