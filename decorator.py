# decorator adds extra features to a function without changing the function's code.
def star_decorator(func):
    def wrapper():  
        """Wrapper function that decorates the original function."""
        print("*****")        # Before the function
        func()                # Original function
        print("*****")        # After the function
    return wrapper

#Now using the  @star_decorator:
@star_decorator
def greet():
    print("Hello!")

greet()
