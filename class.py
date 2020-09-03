records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]

dept_idx = {}

#build the index

for name, dept in records:
    # initialize the lists for each index position of the dictionary
    if dept not in dept_idx:
        dept_idx[dept] = []
    # this part appends each name to the department 
    dept_idx[dept].append(name)

# do quick lookups
print(dept_idx)

# Functions can be utilized to do this work as well


# Where : encode = a dictionary of key values 
# def encrypt(s):
#     result = ''
#     for c in s:
#         result += encode[c]

def decrypt(s):
    result = ''

    for c in s:
        result += encode_table[c]

    return result

# decode_table = {value:key for key, value in encode_table.items()}

# The above is a great example of using dictionary mapping to create
# a new dictionary to use as a decoder
# The below is the same thing
# for key, value in encode_table.items():
# decode_table[value] = key




"""
This code section does the following

In a loop:
    Enter a URL: [URL Here]
    [Shows the data from that URL]

It also caches the data so that more requests for the same URL
simply return the cached data instead of going over the network again.

Stuff to figure out:
    How to get data from a URL
    How are we going to cache it?






import urllib.request

while True:
    url = input("Enter a URL: ")

    with urllib.request.urlopen(url) as response:
        html = response.read()

print(html[:256])

This works for getting stuff from a URL
Now to cache it!
"""

