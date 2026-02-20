with open("c:/Learn-Python-main/harry/chapter 9 partice set/old.txt", "r") as f:
        content=f.read()
        
with open("renamed_by_python.txt", "w") as f:
    f.write(content)
  