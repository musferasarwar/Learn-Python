with open("c:/Learn-Python-main/harry/chapter 9 partice set/this.txt") as f:
    content = f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)
