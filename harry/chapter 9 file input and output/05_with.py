f=open("file.txt")
print(f.read())
f.close()


# the same ca be  written using with statment like this:
with open("file.txt") as f:
    print(f.read())

# you dont have to explicity close the file