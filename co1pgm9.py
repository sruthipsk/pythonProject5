str=input("enter a string=")
f=str[0]
for x in str:
    if x==f:
        n=(str[1:].replace(x,"@"))
    s=f+n
print(s)
