#!/usr/bin/env python

import imaplib

with imaplib.IMAP4("imap.hostname.com") as im:
    im.login("username", "password" )

    print("Existing mailboxes:")
    for mb in im.list()[1]:
        name = mb.split(b'"."')[-1]
        print(" - {}".format(name.decode().strip(' "')))

    mb = input("Which mailbox to display: ")
    im.select(mb)
    status, data = im.search(None, "ALL")
    for mailno in data[0].split():
        type, data = im.fetch(mailno, "(RFC822)")
        print("{}\n+++\n".format(data[0][1].decode()))
    im.close()
