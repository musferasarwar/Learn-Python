# in this problem we learn factoral
# what is factoral
# it's simple  the number is here you can multiple 1 to this number
# like this
# 5! = 1* 2 * 3* 4* 5

n=int(input("enter a number :"))
product = 1
for i in range (1, n+1):
    product = product * i



print (f"the factorail of {n} is {product}")