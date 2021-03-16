List=[]
l=int(input("how many numbrs:"))
for n in range(l):
  li=int(input("enter the num:"))
  List. append(li)
print(List)
for i in List:
  if i%2==0:
    List.remove(i)
print(List)