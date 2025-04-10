a=int(input("Enter your age:"))

if(a>=18):
    print("you above the age of consent")
    print ("good for you")
elif(a<0):
    print("you are entering an invalid age")
    
elif(a==0):
    print("you are entering 0 which is not a valid age")

else:
    print("you below the age of consent")

print("end of program")
