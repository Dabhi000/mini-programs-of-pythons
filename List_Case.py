List = [10,20,"Jaimin",True,90.99]
List[0]=15
print(List)

print(List[-2])
print(List[len(List)-2])
print(List[5-2])
print(List[3])

# print(List[0:4])
# print(List[1:5])

# print(List[-5:])
# print(List[:-1]) # Last position will Ignore.
# print(List[:5])  
print(List[::-1]) # for reverse print.

l = [1,2,3,4,5]
k = [9,6,8,7,10]
print(l.index(1)) # it will gave you index of number 
print("This variable is",l.count(2),"times in List.")

l.append(6) # add new element on last position
l.insert(0,0) # it's take two argument 1 is index and 2 is value

print(l)

l.remove(3) #remove specific value
l.pop() #remove last index value

print(l)

k.sort()
print(k)

k.reverse()
print(k)

l = [1,9,8,4,5]
p = l
print(id(l))
print(p,"p ki id is ",id(p))
o = l.copy()
print(o,"o ki id ", id(o))
print("------------------------")
l.append(20)
print(l)
print("p is ",p)
print("o is ",o)

#List can store multiple datatype values
#You can change the values in List
#List create by square brackets []



# while True:
    
#     p = int(input("Enter The Value:"))
    
#     match p:
        
#         case 0:
#             print("I am Srk")
#         case 1:
#             print("I am Salman")
#         case 2:
#             print("I am Amir")
#         case _:
#             print(p)


# print("Hello", end='......')
# print("Jay Mataji")
# x = lambda a : a - 10
# print(x(5))

# for i in List:
#     if i==20:
#         continue
    
#     print(i)
    
# for i in range(0,5):
#     print(List[i])

# i=0
# while i<5:
#     print(List[i])
#     i+=1

# for i in range(0,6):
#     for j in range(0,6):
#         print(i,end="")
#     print()
