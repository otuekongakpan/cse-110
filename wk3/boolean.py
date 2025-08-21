# there are three boolean statements which are 'not', 'and' and 'or' in order of precedence. 
# 'and' works if both statement are true while or works if one statement is true. 
# 'not' works in reverse

men = int(input("How many men are there? "))
women = int(input("How many women are there? "))

total = men + women

has_enough_players = total == 7
has_enough_women = women == 4 
has_enough_men = men == 3

if has_enough_players and has_enough_women and has_enough_men:
    print("You can play!")
else:
    print("You cannot play.")
if not has_enough_players:
    print("Ask the other team if they want to practice.")