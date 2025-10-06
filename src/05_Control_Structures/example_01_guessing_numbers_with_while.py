#!/usr/bin/env python
secret = 1337
attempt = -1

while attempt != secret:
    attempt = int(input("Guess: "))

    if attempt < secret:
        print("Too small")
    elif attempt > secret:
        print("Too large")

print("You did it!")
