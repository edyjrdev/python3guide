#!/usr/bin/env python

from email.message import Message

msg = Message()
msg.set_payload("This is my self-created email.")
msg["Subject"] = "Hello world"
msg["From"] = "Donald Duck <don@ld.com>"
msg["To"] = "Daisy Duck <d@isy.com>"

print(msg.as_string())

