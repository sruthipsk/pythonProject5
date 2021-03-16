list=[]
num=int(input("how many num:"))
for i in range(num):
    x=int(input("enter the numbers:"))
    if(x<100):
        list.append(x)
    else:
        list.append("over")
print(list)