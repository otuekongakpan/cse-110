#act1
age = input ("How old are you? ")
age_input = int(age)
one = 1
next_age = age_input + one
print(f"On your next birthday, you will be {next_age}")

#act2
cartons = input ("How many egg cartons do you have? ")
eggs_input = int(cartons)
eggs = eggs_input * 12
print(f"You have {eggs} eggs")

#act3
cookies = input ("How many cookies do you have? ")
people = input ("How many people are there? ")

cookies_input = int(cookies)
people_input = int(people)

solution = cookies_input  / people_input  
print(solution)