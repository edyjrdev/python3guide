#!/usr/bin/env python

secret = 1337
attempt = -1
counter = 0

while attempt != secret:
    attempt = int(input("Guess: "))

    if attempt < secret:
        print("Too small")
    if attempt > secret:
        print("Too large")

    counter = counter + 1

print("Great, you did it in", counter, "tries!")
