#Matthew Beer
#09/10/2014
#Iteration class exercise 3

num1 = int(input("Please enter how many numbers are to be averaged: "))
total = 0
for count in range(num1):
    num2 = int(input("Enter a number: "))
    total = num2 + total
average =  total / num1
print("The average is {0}.".format(average))
