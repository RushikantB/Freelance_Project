def addition_decorator(func):
    def wrapper(a, b):
        print(f"Adding {a} and {b} : ")
        result=func(a,b)
        print(f"Result : {result}")
        return result
    return wrapper

@addition_decorator
def add(a, b):
    return a + b

add(5,3)