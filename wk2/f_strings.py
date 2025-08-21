number = 222.5656267

# to round of numbers to the nearest hundreths, you can use the :.2f command
# to the nearest thousandths will be :.3f and so on...... jsyk, this the best
#for every situation. adding an e beside will help format the variable to exponent eg.
# :.3fe, :.8fe etc.
print(f"The number is ${number:.2f}")

# also, we can use the round function like this:
number2 = round(number, 3) 
print(number2)

#if you have a 0 after your first decimal digit, the round 
#function cannot round it off to two decimal places. for example:
number3 = 89.20493
no3_input = round(number3, 2)
print(no3_input)