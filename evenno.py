minimum = int (input("please enter the minium values : "))
maximum = int (input("please enter the maximum values : "))

even_total = 0
odd_total = 0

for number in range(minimum,maximum +1):
    if(number % 2 == 0):
        even_total = even_total + number
    
    else:
        odd_total = odd_total + number

print("the sum of even numbers from 1 to {0} = {1}".format(number,even_total))
print("the sum of odd numbers from 1 to {0} = {1}".format(number,odd_total))