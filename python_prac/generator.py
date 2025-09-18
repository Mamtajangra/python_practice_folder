# define a simple function 
def gen():
    print("hello 1")
    yield 1
    print("end hello 1")
    yield 2
    print("hello 2")
    yield 3
    print("end hello 2")
    yield 4
    print("hello 3")
    yield 5
    print("end hello 3")


# gen()
# store gen in a variable 
gen_object = gen()
# gen_object.__next__()
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))
print(next(gen_object))