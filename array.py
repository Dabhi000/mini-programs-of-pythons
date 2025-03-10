byte_array = bytearray([10,20,30,40,50])

#display
print("initial byte array :")
for element in byte_array:
    print(element,end=" ")
print()

#read and modify 
index = int(input("enter the index of the element to modify (0-4):"))
if index < 0 or index >= len(byte_array):
    print("invalid index!")

else:
    new_value = int(input("enter the value for the element: "))
    byte_array[index] = new_value

#disply the modify array
print("modify byte array")
for element in byte_array:
    print(element, end=" ")
print()   