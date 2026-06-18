marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


age = int(input("Enter age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18:
    if citizen == "yes":
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
else:
    print("Not eligible to vote")


day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")