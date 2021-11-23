import smtplib
import ssl
from config import *


class SendMail:
    def __init__(self, message):
        smtp_server = smtp_server_  # "smtp.gmail.com"
        sender_email = sender_email_
        port = email_port_  # 465 For SSL
        receiver_email = receiver_email_
        password = email_password_
        self.message = message
        # Create a secure SSL context
        context = ssl.create_default_context()
        print("port:", port)
        if port == 465:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                try:
                    server.login(sender_email, password)
                except:
                    print("Error login in")
                else:
                    print("Logged in succesfully")
                    server.sendmail(sender_email, receiver_email, message)
                    print("Email sent to:", receiver_email_)
        elif port == 25:
            # send mail without ssl on port 25 (default)
            with smtplib.SMTP(smtp_server, port) as server:
                try:
                    server.login(sender_email, password)
                except:
                    print("Error login in")
                else:
                    print("Logged in succesfully")
                    server.sendmail(sender_email, receiver_email, message)
                    print("Email sent to:", receiver_email_)
                    server.quit()
                    print("Quit")
                    server.close()
                    print("Closed")
        elif port == 587:
            # send mail without ssl on port 587 (default)
            with smtplib.SMTP(smtp_server, port) as server:
                try:
                    server.login(sender_email, password)
                except:
                    print("Error login in")
                else:
                    print("Logged in succesfully")
                    server.sendmail(sender_email, receiver_email, message)
                    print("Email sent to:", receiver_email_)
                    server.quit()
                    print("Quit")
                    server.close()
                    print("Closed")
        else:
            print("Error: port not supported")
