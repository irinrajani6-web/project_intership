print("args")

def add(*args):
    print(args)

add(10, 20, 30)
print("kwargs")

def student(**kwargs):
    print(kwargs)

student(name="Irin", age=17, city="Ahmedabad")

print("lambda")
add = lambda a, b: a + b

print(add(10, 20))

print("Recursion")
def countdown(n):
    if n == 0:
        print("Done")
    else:
        print(n)
        countdown(n - 1)

countdown(5)