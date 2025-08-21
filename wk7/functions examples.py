def get_positive_value(prompt_text):
    """
    Prompt the user for a value and reprompt them if the 
    original valus is negative.
    """
    # prompt for the value
    value = float(input(prompt_text))
    
    # check if the value is positive and reprompt if needed
    while value < 0:
        print("Sorry, the value cannot be negative")

        value = float(input(prompt_text))
    # return value
    return value

length = get_positive_value ("What is the length of the rectangle? ")
width = get_positive_value ("What is the width of the rectangle? ")

area = length * width

print(f"The area is {area}")