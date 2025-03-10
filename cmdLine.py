import sys

# print(sys.argv)
# print(type(sys.argv))
# print(sys.argv[0])

# for i in sys.argv:
#     print(i)

for i in range(1,len(sys.argv)):
    print(sys.argv[i])

    if int(sys.argv[i])%2==0:
        print("even")
    else:
        print("odd")




# Printing multiplication table
# value=int(sys.argv[1])
# for i in range(0,11):
#     print(value,"*",i,"=",value*i)