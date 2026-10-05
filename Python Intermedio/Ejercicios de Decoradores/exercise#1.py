def print_params_and_return(func):
    def wrapper(*args, **kwargs):

        print(f"Positional arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"Return value: {result}")
        
        return result
        
    return wrapper


@print_params_and_return
def multiply(a, b):
    return a * b

print("Calling the function...")
multiply(5, 4)