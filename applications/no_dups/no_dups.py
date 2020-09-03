from collections import OrderedDict

def no_dups(s):
    
    x = s.split()
    
    m = ''

    for word in x:
        if word not in m:
            m += ' ' + word

    return m



# this returns a string with all duplicates removed
# This is O(n)
# because depending on how long the input is, the function will have to split
# and join more and more words

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))

    #from collections import OrderedDict
    # use as normal dictionary

    # I don't need to use a dictionary for this because I can 
    # iterate through the split list of words, and if it hasn't been
    # added to my answer, I will just concatenate it.