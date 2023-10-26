''' Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0 '''

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
