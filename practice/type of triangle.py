# here we will find out the type of triangles 
def triangle_type(nums):
    # assume first,second,third value == a,b,c respecively 
    a = nums[0]
    b = nums[1]
    c = nums[2]
    # firstly check that triangle is valid like the value of sum of two sides are greater than the third 
    if a+b<c or b+c<a or a+c<b:
        return"not valid"
    # if three sides are equal are equilateral triangle 
    elif a == b == c:
        return"equilateral triangle"
    # if no sides are equal is scalene 
    elif a!=b and b!=c and a!=c:
        return"scalene triangle"
    # two sides are equal is isosceles 
    elif a==b!=c or b==c!=a or a==c!=b:
        return"isosceles triangle"
    


nums = [2,3,2] 
print(triangle_type(nums))