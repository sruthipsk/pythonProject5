
List = []
sum = 0
l = int(input("how many numbrs:"))
for n in range(l):
    li = int(input("enter the num:"))
    List.append(li)
print(List)
for i in List:
    sum = sum + i
print("sum=", sum)