#Matthew Beer
#15/10/14
#Iteration revision exercise 4

num1 = int(input("Please enter a number between 10 and 20: "))
while num1 > 20 or num1 < 10:
    num1 = int(input("The number you have entered is invalid, please enter another number: "))
print("The number you have chosen is within the range")
