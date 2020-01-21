f = open("items.py")
items = {}
total = 0
for line in f:
    info = line.split()
    items[info[0]]= {"price":float(info[1]), "tax":float(info[2])}
    price = float(info[1])*float(info[2])
    total += price

print(items)
print("The total price is:", total, "€")
