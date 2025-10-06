#!/usr/bin/env python
secret = 1337
while (attempt := int(input("Guess: "))) != secret:
    if attempt == 0:
        print("Game will be finished")
        break
    elif attempt < secret:
        print("Too small")
    elif attempt > secret:
        print("Too large")
else:
    print("You did it!")
