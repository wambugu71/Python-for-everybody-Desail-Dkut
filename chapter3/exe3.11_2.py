''' Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input
'''
try:
  hours = float(input("Enter Hours:"))
  rate = float(input("Enter pay:"))
  pay:float = 0.0

  if  hours < 40:
    pay: float  = hours * rate
  else:
    over_time: float = hours - 40
    over_pay: float = over_time * rate
    pay: float  = (1.5 * over_pay * rate) + (rate *40)
  print("Pay: {}".format(pay))
except: 
  print("Error please  enter  numeric  input.")
