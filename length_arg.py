def variable_length(*args):
    for value in range (0,len(args)):
        print(args[value])

variable_length('a','b','c','d','e','f')