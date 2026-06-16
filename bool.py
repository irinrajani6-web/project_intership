print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 100
b = 50

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

print(bool("Python"))
print(bool(100))

x = "Programming"
y = 25

print(bool(x))
print(bool(y))

print(bool("Hello"))
print(bool(123))
print(bool(["Apple", "Banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))

def myFunction():
    return True

print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")

z = 200
print(isinstance(z, int))