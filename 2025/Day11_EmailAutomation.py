# Day11_EmailAutomation.py
# Send email using Python (SMTP)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, password, recipient, subject, body):
    try:
        # Setup MIME
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()

        print(" Email sent successfully!")

    except Exception as e:
        print(f" Error: {e}")


if __name__ == "__main__":
    sender_email = input("Enter your Gmail: ")
    sender_password = input("Enter your Gmail App Password: ")
    recipient_email = input("Enter recipient email: ")
    subject = input("Enter subject: ")
    body = input("Enter message body: ")

    send_email(sender_email, sender_password, recipient_email, subject, body)
