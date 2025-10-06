#!/usr/bin/env python

import poplib

pop = poplib.POP3("pop.server.com")
pop.user("username")
pop.pass_("password")

for i in range(1, pop.stat()[0]+1):
    for line in pop.retr(i)[1]:
        print(line)
    print("***")

pop.quit()

