print("Please enter the following information:")
print()

first_name = input("First name: ")
last_name = input("Last name: ")
email_address = input ("Email address: ")
phone_number = input ("Phone number: ")
job_title = input ("Job title: ")
id_number = input ("ID Number: ")

print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.title()}")
print(f"ID: {id_number}")

print()
print(f"{email_address}")
print(f"{phone_number}")
print("----------------------------------------")


