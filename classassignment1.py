# Declare variables.
num = int()

#Prompt user to enter an integer and determine if it is positive, negative, or zero.
num = int(input("Enter an integer: "))

#Determine if integer is positive, negative, or zero.
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Determine if integer is even or odd.
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("This is the end of my program!")