# 1) Feranhit to Calcious c=5/9(feranhit-32)
# 2) Km to Meter 1 km = 1000 meter
# 3) Gram to Kg 
# 4) Rs to Dollar

feranhit = float(input("Enter Feranhit "))
km = int(input("Enter km "))
gram = int(input("Enter gram "))
rs = int(input("Enter rs "))

c = (feranhit-32)* (5/9)

meter = km*1000

kg = gram/1000

dollar = rs/84

print(f"{feranhit} Feranhit to Calcious is ",c)
print(f"{km} Km to Meter is ", meter)
print(f"{gram} Gram to Kg  is ", kg)
print(f"{rs} Rs to Dollar is ",dollar)