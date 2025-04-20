def rem(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item.replace(word, ""))
    return n

l = ["musfera", "rohan", "shubham", "an"]
print(rem(l, "an"))
