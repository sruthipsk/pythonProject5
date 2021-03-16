n=int(input("enter the limit:"))
list=[]
for i in range(n):
    x=int(input("enter the number:"))
    list.append(x)
print(list)
b=[x for x in list if x>0]
print(b)
list1=[]
num=int(input("how many num:"))
for n in range(num):
    numbers=int(input("enter the numbers"))
    list1.append(numbers)
list1=[x**2 for x in list1]
print(list1)
a="strawberry"
vow="aeiou"
lis=[x for x in a if x in vow]
print("vowels are:",lis)
ab="strawberry"
list2=[ord(x)for x in a]
print("order is:",list2)
