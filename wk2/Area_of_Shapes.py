"""
Shape Area Calculator

Otuekong Akpan

"""

square_side = float (input("What is the length of a side of square in cm? "))
print(f"The area of a square is {square_side**2} cm^2 and {(square_side**2) / 1000} m^2")

r_width = float(input("What is the width of rectangle? "))
r_length = float(input("What is the length of rectangle? "))

print(f"The area of the rectangle is {r_length + r_width:.2f}")

radius = float (input("What is the radius of a circle? "))
print(f"The radius of a circle is {3.14 * radius **2}")
