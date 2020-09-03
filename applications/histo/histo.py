def word_count(text_doc):
    d = {}
    # assign a variable to opening the text file
    x = open(text_doc, "r")
    # we can read the file and output the text with .read()
    x2 = x.read()
    # x2 now holds the reading version of our text file.
    

    print(x2)
    # ignore spaces


word_count('robin.txt')

# How to use backslash
# backslashes escape the character following it
# escape a backslash followed by a backslash

# \\n to target \n