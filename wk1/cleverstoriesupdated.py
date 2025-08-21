start =  input ("Please enter the following information:" )
print(start)

adjective = input ("Adjective: ")
animal1 = input ("First Animal: ")
first_verb = input ("first verb: ")
exclamation = input ("Exclamation: ")
second_verb = input ("verb2: ")
third_verb = input ("verb3: ")

# I decided to add my own line to add to the story
fourth_verb = input ("verb4: ")
fifth_verb = input ("verb5: ")
sixth_verb = input ("verb6: ")
first_noun = input  ("noun: ")

print("Your story is:")
print("")

clever_story = f"""
The other day, I was in trouble. It all started when I saw a very 
{adjective} {animal1} {first_verb} down the hallway. "{exclamation.capitalize()}!" I yelled. But all 
I could think to do was to {second_verb} over and over. Miraculously,
that caused it to stop, but not before it tried to {third_verb} 
right in front of my family.
I ran across the {first_noun}, I {fourth_verb} into an hotel with  {fifth_verb} 
and had a very nice and peaceful {sixth_verb}.
"""

print(clever_story)