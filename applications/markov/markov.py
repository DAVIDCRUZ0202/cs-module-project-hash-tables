import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here
lit = []

for word in words.split():
    lit.append(word)

print(lit)

stop = '.?!"'
for word in lit:
    if word[-1] in stop:
        print(word)
        break
    else:
        print(random.choice(lit))