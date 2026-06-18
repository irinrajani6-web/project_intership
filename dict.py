d = {"name": "Irin", "age": 17, "city": "mahuva"}

print("Original:", d)

x = d.copy()
print("Copy:", x)

print("Get:", d.get("name"))

print("Items:", d.items())

print("Keys:", d.keys())

print("Values:", d.values())

d.update({"age": 18, "course": "IT"})
print("After Update:", d)

d.pop("city")
print("After Pop:", d)

d.popitem()
print("After Popitem:", d)

d.clear()
print("After Clear:", d)