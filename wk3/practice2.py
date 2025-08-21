free_money = input("Do you think you qualify for free money? ")
is_qualified = False

if free_money.lower() == "yes":
    print("Let's see how well you qualify!")

    qualification1 = int(input("How old are you? "))
    if qualification1 < 18:
        print("You do not qualify")
        is_qualified = False
    else:
        print("Next question.")
    qualification2 = input("Do you have a bank account? ")
    if qualification2.lower() == "yes":
        print("Good! Next question.")
        is_qualified = True

        qualification3 = input("Do you have any criminal records? ")
        if qualification3.lower() == "no":
            print("Congratulations! you qualify for 100% free money.")
            is_qualified = True
        elif qualification3.lower() == "yes":
            why = input("What were you charged with? battery, theft, murder, sexual assault, other?  ")
            
            if why == "battery":
                print("Congrats! You qualify for 20% free money")
                is_qualified = True

            elif why == "theft":
                print("Congrats! You qualify for 28% free money")
                is_qualified = True

            elif why == "murder":
                print("Sorry, you do not qualify!")
                is_qualified = False

            elif why == "sexual assault":
                print("Sorry, you do not qualify")
                is_qualified = False

            elif why == "other":
                input("Please specify: " )
                print("Congrats, you qualify for 5% - 15% free money. Here are some questions to answer")
                
                quest1 = int(input("How many years did you spend in jail?  "))
                
                if quest1 >= 15:
                    print("Congrats, you qualify for 5% free money")
                    is_qualified = True
                elif quest1 >= 7:
                    print("Congrats, you qualify for 10% free money")
                    is_qualified = True
                elif quest1 <= 2:
                    print("Congrats, you qualify for 15% free money")
                    is_qualified = True
               
    else:
        print("You do not qualify.")
        is_qualified = False
        
else:
    print("You do not qualify!")
    is_qualified = False

free_money_amount = 2000.00
  
free_money_message = f""""
Note: The free money amount is ${free_money_amount}
You can calculate how much free money you have gotten with our calculator
"""
if is_qualified == True:
    print(free_money_message)

    x = int(input("What  is the percentage free money you recieved? "))

    free_money_calculator = float(free_money_amount * x / 100)
    print(f"You will recieve ${free_money_calculator}")

