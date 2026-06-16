fruits = ["apple", "banana", "cherry"]

fruits.append("orange")
print(fruits)

fruits.insert(1, "mango")
print(fruits)

fruits.extend(["kiwi", "grapes"])
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)

fruits.clear()
print(fruits)

fruits = ["apple", "banana", "cherry"]

print(fruits.index("banana"))

print(fruits.count("apple"))

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

newlist = fruits.copy()
print(newlist)

cars = ["BMW", "Audi"]
fruits.extend(cars)
print(fruits)

print(len(fruits))

print(type(fruits))