#Write a program to find out and display the common and
#the non common elements in the list using membership operators (in and not in)

a = [1, 2, 3, 4,5]
b = [2, 3, 8, 9, 10]
c= []

for i in a:
    if i in b:
        print(i,"is common")
    else:
        print(i,"is not common")

print("==============")
for i in b:
    if i in a:
        print(i,"is common")
    else:
        print(i,"is not common")
    




