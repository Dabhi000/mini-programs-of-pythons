#Write a program to search an element in the list using for loop and also demonstrate the use of “else” with for loop.

def search_element(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            print(f"Element {target} found at index {index}")
            break
    else:
        print(f"Element {target} not found in the list")

# Example usage
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Get user input
search_item = int(input("Enter the element you want to search for: "))

# Perform the search
search_element(my_list, search_item)