animal = input("What is your favourite animal? ")
animal = animal.lower()

sound = ""

if animal == "dog":
    sound = "woof woof"
elif animal == "cat":
    sound = "meow"
else:
    sound = "unknown"

print(f"The {animal} makes the sound: {sound}")