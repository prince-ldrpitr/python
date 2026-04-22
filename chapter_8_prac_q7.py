def remove(l,word):
    for item in l:
        l.remove(word)
        return l



l = ["  apple  ", "banana", "  mango ", "apple", "grapes  "]
print(remove(l,"apple"))