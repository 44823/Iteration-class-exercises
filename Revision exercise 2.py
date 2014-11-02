#Matthew Beer
#12/10/14
#Iteration revision exercise 2

message = input("Please enter your message: ")
num1 = int(input("How many times would you like the message to be repeated? "))
for count in range (num1):
    print("{0}".format(message))
    
