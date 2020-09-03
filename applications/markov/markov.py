import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

x = words.split()

d = {}

for word in x:
    next = next(x(word))
    if word not in d:
        d[word] = []
    if next not in d[word]:
        d[word].append(next)



print(d)
    

# TODO: construct 5 random sentences
# Your code here

# for word in words.split():
#     lit.append(word)

# print(lit)

# stop = '.?!"'
# for word in lit:
#     if word[-1] in stop:
#         print(word)
#         break
#     else:
#         print(random.choice(lit))

# Create 5 sentences
# use a 