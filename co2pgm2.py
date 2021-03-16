n=int(input("Enter the Limit"))
x=0
y=1
print(x)
print(y)
for i in range(2, n):
  sum=x+y
  print(sum)
  x=y
  y=sum