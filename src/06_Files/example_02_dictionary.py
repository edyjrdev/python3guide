#!/usr/bin/env python
words = {}
with open("dictionary.txt", "r") as fobj:
    for line in fobj:
        line = line.strip()
        assignment = line.split(" ")
        if len(assignment) == 2:    # consider only valid lines
            words[assignment[0]] = assignment[1]

while True:
    word = input("Enter a word: ")
    if word in words:
        print("The German word is:", words[word])
    else:
        print("The word is unknown")
