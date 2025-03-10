list1=[1,2,3,3,4,5,6,6,6,7,8,9,11,12,13,4,2,1]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
