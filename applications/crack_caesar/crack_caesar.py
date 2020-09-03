# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# use a with statement to open the text, and save it to a variable
with open('ciphertext.txt', 'r') as f:
    words = f.read()


# bad characters do not need to get deciphered
bad_chars = ('\n',' ','!','"','(',')',',','.','1',':',';','?','-')

#initiate a blank dictionary for counting characters
char_count={}

#loop through each word
for i in words:
    # if the word is being counted
    if i in char_count:
        # add 1
        char_count[i] += 1
    # if the word isnt in the count yet
    else:
        # initialize it to 1
        char_count[i] = 1
# for each character in the bad chars
for i in bad_chars:
    # take that character out of char_count
    char_count.pop(i)

#now we create a sorted version of the character count. 
# this makes our encoded character counter sort the maximum values to the beginning of the dictionary
char_count = dict(sorted(char_count.items(),key = lambda x: x[1], reverse=True))

# take out the blanks
char_count.pop("'")

#now to match the encoded frequencies with the proper ones

#same with statement for the readme
with open('README.md', 'r') as f:
    readme = f.readlines()


#initialize a list for frequencies
char_frequency = []

for i in readme:
    if i[:2] == '| ':
        char_frequency.append(i[1:6].strip())

char_frequency.pop(0)

for a,b in zip(char_count, char_frequency):
    char_count[a] = b

for i in words:
    try:
        if i in bad_chars:
            print(i,end='')
        else:
            print(char_count[i],end='')
    except KeyError:
        continue