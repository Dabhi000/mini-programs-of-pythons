# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#Methods -> fromkeys, get, items, keys, pop, popitem, setdefault, update, values


# dic = {
#     "name":"jaimin",
#     "age":12
# }

# dic["name"]="ketan"
# print(dic)
# print(type(dic))
# print(dic["name"])

dic2 = {
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:'Sunday'
}
# print(dic2[1])
print(dic2.keys())
print(dic2.values())

Phone = {
    'Apple':{
        'iphone_13':100000,
        'iphone_14':110000,
        'iphone_15':120000
    },
    'Samsung':{
        'fold3':120000,
        'fold4':130000,
        'fold5':140000
    },
    "Reame":{
        'realme6':15000,
        'realme7':20000,
        'realme8':30000
    }
}

#print(Phone["Apple"]['iphone_13'])
#print(Phone["Samsung"]['fold4'])
for x, obj in Phone.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])


Animal = {
    "bird":"peacock",
    "mamls":"cow",
    "fish":"shark",
    "reptiles":"python",
    "videsi":"emu"
}

# k = Animal.items()
# print(k)

# Animal.update({"fish": "starfish"})
# print(k)

Animal["Nonveg"]="Lion"
Animal["veg"]="goat"
print(Animal)
Animal.pop("videsi")
print(Animal)