import os 

# specify the directory you want  to list
directory_path ='/new folder'

# list all files directories n the sepcified path
contents = os.listdir(directory_path)

# print each file  and directory  name 
for item in contents:
    print(item )
