def check_only_numbers(func):
    def wrapper(*args, **kwargs):
        all_values = list(args) + list(kwargs.values())

        for value in all_values:

            if not isinstance(value, (int, float)):
                raise TypeError(f"All parameters must be numbers. Invalid parameter found: {value}")

        return func(*args, **kwargs)
        
    return wrapper


@check_only_numbers
def calculate_area(length, width):
    return length * width

print("Test 1:")
result = calculate_area(10, 5.5)
print(f"Area: {result}")

print("\nTest 2:")
calculate_area(10, "cinco")