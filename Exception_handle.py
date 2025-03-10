val = input("Enter a number")
va = input("enter b")

try:
    for i in range(0,6):
        print(val*va)
except Exception as e:
    print(e)
finally:
    print("I am always print")


print("IMP Lines")

#throw customs errors
val = int(input("Enter a number"))

if(val>5 or val<10):
    raise ValueError("Entered Value is incorrect")


