print("You must be 18 or above to register")
age = int(input("How old are you? "))

while age < 18:
    print("You must be 18 years or older to continue. Try again")
    age = int(input("How old are you? "))
    
print("You are in")