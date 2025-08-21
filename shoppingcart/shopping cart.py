# I added a discount calculator for users when they spend $100 or more
options = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]
carts = []
cart_prices = []
item = []
running = True

print("Welcome to Shopping Cart Program!")
while running:
    print("Please select one of the following: ")

    for i  in range(len(options)):
        option = options[i]
        normal_count = i + 1
        print(f"{normal_count}. {option}")
    user_choice = input("Please enter an action: ")

    if user_choice == "1":
        new_carts = ""
        while new_carts != "quit":
            new_carts = input("What item would you like to add? ")
            if new_carts != "quit":
                carts.append(new_carts)
                cart_price = float(input(f"What is the price of {new_carts.title()}? "))
                cart_prices.append(cart_price)
                print(f"'{new_carts.title()}' has been added to the cart")

    elif user_choice == "2":
        print("The contents of the shopping lists are:")
        for i in range(len(carts)):
            new_cart = carts[i]
            normal_count = i + 1
            
            print(f"{normal_count}. {new_cart} - ${cart_prices[i]:.2f}")

    elif user_choice == "3":
        if not carts:
            print("Your cart is empty, nothing to remove.")
        else:
            print("\nYour shopping cart:")
            for i in range(len(carts)):  
                print(f"{i + 1}. {carts[i]} - ${cart_prices[i]:.2f}")  

            item_index = int(input("Enter item number to remove (or 0 to cancel): ")) - 1  

            if 0 <= item_index < len(carts):  
                removed_item = carts.pop(item_index)  
                removed_price = cart_prices.pop(item_index)  
                print(f"'{removed_item}' has been removed from the cart. Price was ${removed_price:.2f}")  
            else:  
                print("Invalid selection, try again.")  
    
    elif user_choice == "4":
        if cart_prices:
            total_price = sum(cart_prices)
            print(f"Total cost of items in cart: ${total_price:.2f}")
            discount = 0  
            if total_price >= 1000:  
                discount = 0.25  # 25% off  
            elif total_price >= 500:  
                discount = 0.20  # 20% off  
            elif total_price >= 200:  
                discount = 0.15  # 15% off  
            elif total_price >= 100:  
                discount = 0.10  # 10% off  

            discounted_price = total_price - (total_price * discount)  

            print(f"Total cost before discount: ${total_price:.2f}")  
            print(f"Discount applied: {discount * 100:.0f}%")  
            print(f"Final total after discount: ${discounted_price:.2f}") 

    elif user_choice == "5":
        print("Thank you for using the Shopping Cart Program. Have a nice day!")
        running = False
