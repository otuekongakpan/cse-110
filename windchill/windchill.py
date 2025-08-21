def get_windchill_fahrenheit(temp_f):

    if -100 <= temp_f <= 1000:
            wind_speeds = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
            for wind_speed in wind_speeds:
                wind_chill = 35.74 + (0.6215 * temp_f) - 35.75 * (wind_speed ** 0.16) + (0.4275 * temp_f * (wind_speed ** 0.16))
                print(f"At temperature {temp_f:.2f}F, and wind speed {wind_speed} mph, the wind chill is {wind_chill:.2f}°F")               
                
    else:
        print("Invalid input. Try again")

def get_windchill_celsius(temp_c):
    
    if -100 <= temp_c <= 1000:
            temp_f = (temp_c * 9/5) + 32
            wind_speeds = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
            for wind_speed in wind_speeds:
                wind_chill = 35.74 + (0.6215 * temp_f) - 35.75 * (wind_speed ** 0.16) + (0.4275 * temp_f * (wind_speed ** 0.16))
                wind_chill_c = (wind_chill - 32) * 5/9
                print(f"At temperature {temp_c}C, and wind speed {wind_speed} mph, the wind chill is {wind_chill_c:.2f}°C")

    else:
        print("Invalid input. Try again")

def get_windchill():
    temp = float(input("What is the temperature? "))
    degree = (input("Fahrenheit or Celcius (F/C)? ")).lower()
    if degree == "f":
        get_windchill_fahrenheit(temp)
    elif degree == "c":
        get_windchill_celsius(temp)
    else:
        print("Invalid input choose between Fahrenheit or Celsius (F/C)")

get_windchill()


   
    




