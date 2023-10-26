'''Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
converted temperature. '''

celsius= float(input("Enter the  number  of degrees °C:"))
F = (celsius * 9/5) + 32

print("{} celsius is {} Fahrenheit".format(celsius, F))