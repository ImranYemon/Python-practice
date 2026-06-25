# Determine if a fruit is ripe , overripe or unripe based on color (green-unripe , yellow-ripe , brown-overripe)

fruit = "banana"

fruit_color_input = input("enter the color \n green , yellow , brown \n : ")
fruit_color = fruit_color_input.lower()

if fruit_color in "green" : 
    print("unripe")
elif fruit_color in "yellow":
    print("ripe")
elif fruit_color in "brown":
    print("overripe")
else: 
    print("wrong entry")


