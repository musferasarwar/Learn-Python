word = "donkey"


with open(r"C:\Learn-Python-main\harry\chapter 9 partice set\file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open(r"C:\Learn-Python-main\harry\chapter 9 partice set\file.txt", "w") as f:
    f.write(contentNew)
