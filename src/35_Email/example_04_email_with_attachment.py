#!/usr/bin/env python

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg["Subject"] = "Hello world"
msg["From"] = "Donald Duck <don@ld.com>"
msg["To"] = "Daisy Duck <d@isy.com>"
text = MIMEText("This is my self-created email.")
msg.attach(text)

with open("coffee.png", "rb") as f:
    image = MIMEImage(f.read())
msg.attach(image)

print(msg.as_string())

