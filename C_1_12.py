#  Write a python program that asks the user to enter a
# length in centimeters. If the user enters a negative
# length, the program should tell the user that the entry is
# invalid. Otherwise, the program should convert the
# length to inches and print out the result. (2.54 = 1 inch).


def cm_to_inches(cm):
    return cm / 2.54

# Ask user for input
length_cm = float(input("Enter a length in centimeters: "))

# Check if the input is valid
if length_cm < 0:
    print("Invalid entry. Length cannot be negative.")
else:
    # Convert to inches and print the result
    length_inches = cm_to_inches(length_cm)
    print(f"{length_cm} centimeters is equal to {length_inches:.2f} inches.")