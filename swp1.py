Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  # Function to swap two numbers
... def swap_numbers(a, b):
...     print("Before swapping:")
...     print(f"a = {a}, b = {b}")
... 
...     # Swapping using tuple unpacking
...     a, b = b, a
... 
...     print("After swapping:")
...     print(f"a = {a}, b = {b}")
...     
... # Example usage
... a = 5
... b = 10
