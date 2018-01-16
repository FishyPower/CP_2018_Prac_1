#Computing Practical 1 - Task 2

radius = input("Input radius in cm: ")

#Obtain radius

length = input("Input length in cm: ")

#Obtain length

pi = 3.1416

#Define the value of pi to 5 significant figures

area = radius * radius * pi

#Calculate area

print("Area of the cylinder is {0} cm2" .format(area))

#Display area

volume = area * length

#Calculate volume

print("Volume of the cylinder is {0} cm3" .format(volume))

#Display volume