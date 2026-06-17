t = ("apple", "banana", "mango")
print(t)

t = t + ("orange",)
print(t)

l = list(t)
l[1] = "grapes"
t = tuple(l)
print(t)

l.remove("apple")
t = tuple(l)
print(t)

nested = (("apple", "banana"), ("mango", "orange"))
print(nested)

del t
print("Tuple Deleted")