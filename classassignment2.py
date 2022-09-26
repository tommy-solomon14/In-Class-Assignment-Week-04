#Declare variables.
month = int()

# Ask user to enter month.
month = int(input("Number of month: "))

#Determine what quarter the month lies in.
if month >= 1 and month <=3:
    print("first quarter")
elif month >= 4 and month <= 6:
    print("second quarter")
elif month >= 7 and month <= 9:
    print("third quarter")
elif month >= 10 and month<= 12:
    print("fourth quarter")
else:
    print("Invalid number, please try again")

#Here to clarify this is the end of the program.
print("This is the end of my program!")