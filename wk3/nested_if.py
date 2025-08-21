temperature = int(input("What is the temperature outside? "))

if temperature < -15:
    print("Stay indoors")
elif temperature < 5:
    weather = input("What is the weather like? sunny, cloudy, rainy or snowy? ")

    if weather.lower() == "sunny":
        print("Go for that run!")
    elif weather.lower() == "rainy":
        print("Go for it but pack some rain gear!")
    elif weather.lower() == "snowy":
        print("Do not go out!")
    elif weather.lower() == "cloudy":
        print("Go for the run but watch the weather!")
    else:
        print("I do not understand your response! Try again.")

else:
    print("Enjoy your run!")