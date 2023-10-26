'''Exercise 3: Write a program to prompt the user for hours and rate per
hour to compute gross pay'''

hours = int(input("Enter Hours:"))
rate = int(input("Enter pay:"))
pay  = hours * rate
print("Pay: {}".format(pay))