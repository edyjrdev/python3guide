#!/usr/bin/env python
secret = 1337
attempt = -1

while attempt != secret:
    attempt = int(input("Guess: "))

    if attempt == 0:
        print("Game will be finished")
        break
    elif attempt < secret:
        print("Too small")
    elif attempt > secret:
        print("Too large")
else:
    print("You did it!")
