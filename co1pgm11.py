list=[]
n=int(input("how many numbers:"))
for n in range(n):
    num=int(input("enter the num:"))
    list.append(num)
print("biggest num in the list is:",max(list))