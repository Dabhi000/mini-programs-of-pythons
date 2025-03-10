#Create a program to display memory locations of two variables using id() function, and then use identity
# operators(is and is not) two compare whether two objects are same or not.


# Create two variables with the same value
a = 5
b = 5

# Create two variables with different values
c = 10
d = [1, 2, 3]

# Display memory locations using id() function
print(f"Memory location of a: {id(a)}")
print(f"Memory location of b: {id(b)}")
print(f"Memory location of c: {id(c)}")
print(f"Memory location of d: {id(d)}")

# Compare objects using identity operators
print(f"\nIs a the same object as b? {a is b}")
print(f"Is a not the same object as c? {a is not c}")
print(f"Is c the same object as d? {c is d}")