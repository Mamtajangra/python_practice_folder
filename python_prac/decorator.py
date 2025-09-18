# 1st decorator .. a function is define inside a function
def decorator1(func):
    # wrapper function 
    def wrapper(*args,**kwargs):
        print("HELLO")
        func()
        print("JU")
    return wrapper


# 2nd decorator 
def decorator2(func):
    def wrapper(*args,**kwargs):
        print("HELLO")
        func()
        print("JU")
    return wrapper


# 3rd decorator 
def decorator3(func):
    def wrapper(*args,**kwargs):
        print("HELLO")
        func()
        print("c++")
    return wrapper


# 4th decorator 
def decorator4(func):
    def wrapper(*args,**kwargs):
        print("python")
        func()
        print("linux")
    return wrapper

    

@decorator1
@decorator2
@decorator3
@decorator4


# define a function
def greet():
    # we want to print hello 
    print("MAMTA")

# call main function
greet()    


