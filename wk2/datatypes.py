song1 = "213 seconds" #this is a string
song2 = 213 #this is an integer (int)
song3 = 213.5  # this is a float

song4 = 188
song5  = 290.55
#python does not allow us to add strings and integers together. I would need to covert the string 
#into an integer to be able to run the code perfectly
#now to do this, i can change song6 to look like this "int(song6)"
song6 = input("What is the length of this song? ")
song7 = input("What is the length of this song? ")
song6_input = int(song6)

#The same works for floats
song7_input = float(song7)

playlist = song4 + song5 + song6_input + song7_input

print(f"The length of your song list is {playlist} seconds long")



