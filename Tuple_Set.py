# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#Methods -> count, index

#Set items are unordered, unchangeable, and do not allow duplicate values.
# set = {"Jaimin","Hiral","Kano"}
# print(set)
# print(type(set))
#Methods -> add, clear, copy, difference, discard, intersection, isdisjoint, issubset, issuperset, pop, remove, symmetric_difference, union

tpl = (1,'2',3,'4')
print(tpl)
print(type(tpl))

# for i in range(6):
#     print(i," is ",tpl.count(i)," times")
print(tpl.index(3))

set1 = {"Jaimin","Hiral","Kano"}

print(set1)

set1.add("Rakshita")
print(set1)