#Computing Practical 1 - Task 4

integer = input("Input integer: ")

#Obtain integer

digit1 = integer%10

#Obtain digit in "ones" place

integer = integer//10

#Remove digit in "ones" place

digit2 = integer%10

#Obtain digit in "tens" place

integer = integer//10

#Remove digit in "tens" place

digit3 = integer%10

#Obtain digit in "hundreds" place

integer = integer//10

#Remove digit in "hundreds" place

sum = digit1 + digit2 + digit3 + integer

print("Sum of the digits is: {0}".format(sum))