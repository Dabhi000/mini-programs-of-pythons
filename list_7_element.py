list1 = [i for i in range (1,8)]
print(list1)
list1.append(8)
print(list1)
list1.insert(2,12)
print(list1)
list2=list1.copy()
print(list2)
another_list=['a','b','c']
list1.extend(another_list)
print(list1)
print(list1.count(3))
list1.remove('c')
print(list1)
print(list1.pop())
list2=[4,8,3,4,6,4,5,68,33,46,5,0]
list2.sort()
print(list2)
list1.reverse()
print(list1)
list2.clear()
print(list2)