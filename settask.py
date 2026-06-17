set1 = {"apple", "banana", "cherry"}
set2 = {"apple", "mango", "orange"}

print("Set1:", set1)
print("Set2:", set2)

print("Union:", set1.union(set2))
print("Union using |:", set1 | set2)

set3 = set1.copy()
set3.update(set2)
print("Update:", set3)

print("Intersection:", set1.intersection(set2))
print("Intersection using &:", set1 & set2)

set3 = set1.copy()
set3.intersection_update(set2)
print("Intersection Update:", set3)

print("Difference:", set1.difference(set2))
print("Difference using -:", set1 - set2)

set3 = set1.copy()
set3.difference_update(set2)
print("Difference Update:", set3)

print("Symmetric Difference:", set1.symmetric_difference(set2))
print("Symmetric Difference using ^:", set1 ^ set2)

set3 = set1.copy()
set3.symmetric_difference_update(set2)
print("Symmetric Difference Update:", set3)