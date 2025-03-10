#Write a program to create a byte type array, read, modify,and display the elements of the array

import array
a = array.array('b', [1, 2, 3, 4, 5])
print(a)
a[0] = 10
print(a)