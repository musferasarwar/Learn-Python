words = ["donkey","but","musfera","lion","bad"] 

with open(r"C:\Learn-Python-main\harry\chapter 9 partice set\files.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open(r"C:\Learn-Python-main\harry\chapter 9 partice set\files.txt", "w") as f:
    f.write(content)
