a = 10
b = 20

list = [1,2,3,4,5];

if (a in list):
    print("line 1 - a is available in given list")

else:
    print("line 1 - a is not available in not given list")

if (b not in list):
    print("line 2 - b is not available in not given list")

else:
    print("line 2 - b is available in given list")

a = 2

if (a in list):
    print("line 3 - a is available in given list")

else:
    print("line 3 - a is not available in given list")

