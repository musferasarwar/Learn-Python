with open("c:/Learn-Python-main/harry/chapter 9 partice set/this.txt", "r") as f:
    content1=f.read()
  
with open("c:/Learn-Python-main/harry/chapter 9 partice set/file.txt", "r") as f:
        content2=f.read()


if(content1 == content2):
    print("yes these file are identical")
    

else:
    print("no these file are not identical")