temperature = float(input("What is your temperature in degrees Celsius? "))
if temperature > 40.5:
    print("Go to the Hospital!")
elif temperature > 39.4:
    print("Call your doctor.")
else:
    print("Consider rest or medicine.")
print("Have a good day.")

# There are many options for the condition, but usually it has the form of x == y or x > y or something similar.
# Don't forget that when you want to see if two items are equal you must use two equals symbols == not just one.
# In most programming languages, including Python, one equals sign = is used to assign a value to a variable, whereas two equal signs == are used to check if two variables are equal.