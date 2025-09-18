# find the  youngest among the 4 students  using if statement 
x=int(input("enter the age of the people 1:"))
y=int(input("enter the age of the people 2:"))
z=int(input("enter the age of the people 3:"))
m=int(input("enter the age of the people 4:"))
if x < y and x < z and x < m:
    print(x)
elif y < x and y < z and y < m:
    print(y)
elif z < x and z < y and z < m:
    print(z)
elif m < x and m < y and m < z:
    print(m)   