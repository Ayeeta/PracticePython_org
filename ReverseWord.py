def reverseWord(anystring):
    x = anystring.split()
    return " ".join(x[::-1])


print(reverseWord('Elijah is my brother'))