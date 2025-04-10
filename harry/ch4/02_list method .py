friend = ["apple", "orange", "musfera", "malaika", 32.45, 44, "false"]
print( friend )  

friend.append("iqra")
print (friend)#friend = ["apple", "orange", "musfera", "malaika", 32.45, 44, "false"]

friend.extend("kishwar")
print (friend) #(k,i,s,h,w,a,r)

l1=[11,34,65,98,0,65]
l1.sort()
print (l1)#[0, 11, 34, 65, 65, 98]

m1=[92,29,48,0,42]
m1.reverse()
print(m1)#[42, 0, 48, 29, 92]

p1 = [34, 39, 36, 0, 46]
p1.insert(2, 99)  # Insert 99 at index 2
print(p1) #[34, 39, 99, 36, 0, 46]

o1=[12,67,49,48,45,68]
print (o1.pop(3))
print(o1)#48    [12,67,49,45,68]

# one method is 
# value=o1.pop(3)
# print(value)
# print (o1)

k1 = [86, 77, 98, 69, 87]
k1.remove(69)  # Removes the first occurrence of 69
print(k1)#[86, 77, 98, 87]
