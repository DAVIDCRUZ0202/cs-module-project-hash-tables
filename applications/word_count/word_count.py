def word_count(s):
    d = {}
    x = s.split()
    for word in x:
        for i in word:
            if i.isalnum() == False:
                word = word.replace(i, '')
        word = word.lower()
        if word == '':
            continue
        elif word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d
        



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))