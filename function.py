def starmethod():
 
    start = int(input("Enter starting rows: "))
    end= int (input("enter the ending rows: "))
    for i in range(start, end+1):
        print("* " * i)
    for i  in range (start, -1 ,end+1):
        print("*"*i)

starmethod()

def sum_numbers():
    n = int(input("Enter a number: "))
    
    total = 0
    for i in range(1, n + 1):
        total += i

    print("Sum =", total)

sum_numbers()
