for i in range(1, 6):
    print("* " * i)

print("reverse")
for i in range(5, 0, -1):
    print("* " * i)

start = int(input("Enter starting rows: "))
end= int (input("enter the ending rows: "))
for i in range(start, end+1):
    print("* " * i)
for i  in range (start, -1 ,end+1):
    print("*"*i)