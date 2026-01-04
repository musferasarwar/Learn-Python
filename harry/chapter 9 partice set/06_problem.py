with open("c:\Learn-Python-main\harry\chapter 9 partice set\log.txt", "r") as f:
    content = f.read()

if "python" in content.lower():
    print("yes python is present")
else:
    print("no python is not present")
