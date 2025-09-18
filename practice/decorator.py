def decorator(func):
    def wrapper (*arg,**kwargs):
        print("start")
        func()
        print("end")
    return wrapper 
   
    


@decorator
def sum():
    print("hello")
sum()