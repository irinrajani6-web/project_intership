fruits = {"apple", "banana", "mango"}
print(fruits)
fruits.add("orange")

if "apple" in fruits:
    print("apple is available in set")

if "grapes" not in fruits:
    print("grapes is not available in set")

print("Set:", fruits)

fruits.remove("banana")
print("After Delete:", fruits)

del fruits
print("Set Deleted")

