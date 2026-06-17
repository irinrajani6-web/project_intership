set1 = {"apple", "banana", "cherry"}
set2 = {"apple", "mango", "orange"}

print("Union:", set1.union(set2))
print("Union Symbol:", set1 | set2)

set1.update(set2)
print("Update:", set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"apple", "mango", "orange"}

print("Intersection:", set1.intersection(set2))
print("Intersection Symbol:", set1 & set2)

set1.intersection_update(set2)
print("Intersection Update:", set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"apple", "mango", "orange"}

print("Difference:", set1.difference(set2))
print("Difference Symbol:", set1 - set2)

set1.difference_update(set2)
print("Difference Update:", set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"apple", "mango", "orange"}

print("Symmetric Difference:", set1.symmetric_difference(set2))
print("Symmetric Difference Symbol:", set1 ^ set2)

set1.symmetric_difference_update(set2)
print("Symmetric Difference Update:", set1)