import smtplib
import ssl
from config import *


class SendMail:
    def __init__(self, receiver_email, message):
        smtp_server = smtp_server_  # "smtp.gmail.com"
        sender_email = sender_email_
        port = email_port_  # 465 For SSL
        self.receiver_email = receiver_email
        password = email_password_
        self.message = message
        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            try:
                server.login(sender_email, password)
            except:
                print("Error login in")
            else:
                print("Logged in succesfully")
                server.sendmail(sender_email, receiver_email, message)
                print("Email sent to:", receiver_email_)
