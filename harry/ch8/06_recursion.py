'''
factorail = (1) 1
factorail = (2) 2*1
factorail = (3) 3*2*1
factorail = (4) 4*3*2*1
factorail = (5) 5*4*3*2*1

factorail(n)=n * (n-1)*...............3*2*1
factorail(n) =n* factorail(n-1)
'''

def factorial(n):
    if n==1or n==0:
        return 1
    return n* factorial(n-1)

n=int(input("Enter a number:"))
print(f"the factorial of this number is: {factorial (n)}")
    