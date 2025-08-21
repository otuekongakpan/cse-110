# index =   0       1         2        3
colours = ["red", "green", "blue", "yellow"]

# print(colours[1])

#for colour in colours:
    #print(colour)

colours.pop(1)
colours.insert(1, "pink")
for i in range(len(colours)):
    colour = colours[i]
    normal_count = i + 1
    print(f"{normal_count}. {colour}")
