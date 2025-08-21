# I decided to add a lot more levels to the game

print("Game Title: The Abandoned Mansion")
print("Game Genre: Adventure")

print()
print("By Otuekong Akpan")

item1 = "ancient key"
item2 = "candle"
anc_act1 = "follow"
anc_act2 = "turn back"
anc_act3 = "wipe"
anc_act4  = "search"
anc_act5 = "investigate"
anc_act6 = "destroy"
anc_act7 = "tear"
anc_act8 = "burn"

game_start = input(f"""
You step through the rusted iron gates of the Ingrid Mansion, its towering walls whispering secrets of a forgotten past.
The moonlight barely touches the cracked cobblestone path ahead.

As you approach the entrance, the heavy wooden door creaks open, as if inviting you inside.
Inside, dust settles over elegant but decayed furniture, and the faint scent of old parchment lingers in the air.
                   
On a small wooden table, you find two items: an {item1.upper()} and a {item2.upper()}.

Which one do you want to pick up?
""")

if game_start.lower() == "ancient key":
    print()
    print("""Feels strangely warm, carved with odd symbols.
As soon as you touch it, a whisper calls your name from the end of the hallway.""")
    
    user_choice = input(f"Do you want to {anc_act1.upper()} the whisper, or {anc_act2.upper()} toward the exit? ")

    if user_choice.lower() == "follow":
        print("""You step cautiously down the hallway, drawn by the eerie voice.
The corridor leads to a grand study, bookshelves towering above you, filled with ancient texts.
              
At the center of the room stands a mirror, covered in dust.""")
        print()

    elif user_choice.lower() == "turn back":
        print("""As you approach the door, it slams shut.
Something wants you to stay.
You must find another way out.
>>>>GAME OVER<<<< 
Thank you for playing!""")
        exit()

    else:
        print("That is not an option, try again")
    
    user_choice2 = input(f"Do you {anc_act3.upper()} the mirror to look inside, or {anc_act4.upper()} the bookshelf for answers? ")
    print()
    if user_choice2.lower() == "wipe":
        print("""Your reflection distorts—it’s not you. A shadowy figure emerges from the glass
It forces it's way through the glass and consumes you
>>>>GAME OVER<<<<
Thank you for playing!""")
        exit()
        
    elif user_choice2.lower() == "search":
        print("""You find a leather-bound journal detailing a ritual and warnings about what still roams the mansion.
              
You brush off the dust and open the leather-bound journal, its pages brittle from time.
Faded ink describes a ritual performed centuries ago—a ceremony meant to seal something away beneath the mansion.
              
At the bottom of the page, you notice a warning scribbled in shaky handwriting:
"Do not break the seal. It cannot be contained a second time."
              
The room grows eerily silent.
              
A shadow moves across the wall, though nothing is there.
""")
    else:
        print("That is not an option, try again")

    user_choice3 = input(f"Do you {anc_act5.upper()} the ritual further or {anc_act6.upper()} the journal? ")

    if user_choice3.lower() == "investigate":
        print("""You flip to the next pages, revealing scattered diagrams of arcane symbols.
Some pages are missing, torn from the book in desperation. A single phrase repeats throughout:
              
"It feeds on fear."
>>>>GAME OVER<<<<
Thank you for playing!
""")
        
    elif user_choice3.lower() == "destroy" :
        print(f"""Fear grips you—what if reading further invites the entity back?
Perhaps burning it will erase its presence forever.""")

        user_choice4 = input(f"There are two ways to destroy the journal. {anc_act7.upper()} it into pieces or {anc_act8.upper()} into ashes. Select one: ")
        if user_choice4.lower() == "tear":
            print("""You tore the journal page by page till  the last piece" 
Upon tearing the last page, a screeching noise is heard" 
                  
It seems like what ever might have been lurking around is now freed into the world 
>>>>GAME OVER<<<<
Thank you for playing!""")
            exit()
            
        elif user_choice4.lower() == "burn":
            print("""You set the journal ablaze and a scary sound like that of a human on fire is heard
Seems like whatever was creeping around must have been burnt with the flame.
                  
OR IS IT JUST THE BEGINNING?
>>>>GAME OVER<<<<
Thank you for playing!""")
            exit()

    else:
        print("That is not an option, try again")

elif game_start.lower() == "candle":
    print(""" You lift the ancient candle and strike a match.
Its glow flickers as shadows twist along the walls, revealing faint footprints on the dusty floor.
          
Ahead, a grand staircase descends into the depths of the mansion. 
Something moves with great speed at the bottom. It was faster than a normal human """)
    
    cand_act1 = "descend"
    cand_act2 = "blow out"
    cand_act3 = "open"
    cand_act4 = "examine"
    cand_act5 = "run"
    cand_act6 = "investigate"

    cand_choice = input(f"Do you {cand_act1.upper()} the stairs to check it out, or {cand_act2.upper()} the candle and hide? ")

    if cand_choice.lower() == "descend":
        print("""The stairs groan beneath your weight as you step into a dimly lit corridor.
A massive iron door stands ahead, covered in intricate carvings.
Next to it, a rusted chest sits half-open.""")
    cand_choice2 = input(f"Do you {cand_act3.upper()} the rusted chest or {cand_act4.upper()} the body of the chest? ")

    if cand_choice2.lower() == "open":
        print(""" You then see a note
You open it
        
It reads: "YOU SEEK WHAT IS NOT LOST AND CHERISH WHAT DOES NOT EXIST"
>>>>GAME OVER<<<< 
Thank you for playing!""")
        exit()

    elif cand_choice2.lower() == "examine":
        print(""" You examine the body of the chest and see something strange.

There is a writing on the body of the chest that reads:
OPEN. I DARE YOU!
>>>>GAME OVER<<<< 
Thank you for playing!""")
        exit()
        
    elif cand_choice.lower() == "blow out":
        print("""The room sinks into total darkness, and you press against the wall, listening.
The sound of heavy breathing fills the space. Then, footsteps. Slow, deliberate. Stopping right next to you.
>>>>GAME OVER<<<< 
Thank you for playing!""")
        exit()
        
    else:
        print("That is not an option, try again")

        
else:
    print("That is not a choice. Try again!")