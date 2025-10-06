#!/usr/bin/env python

import email

mail = """Subject: Hello world
From: Donald Duck <don@ld.com>
To: Daisy Duck <d@isy.com>

Hello world
"""

msg = email.message_from_string(mail)
print(msg["From"])


