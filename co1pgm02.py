y1=int(input("enter current year:"))
y2=int(input("enter last year:"))
print("fucture leap years are:")
for x in range (y1,y2+1):
    if(x%4==0 and x%100!=0 or x%400==0):
       print(x)
