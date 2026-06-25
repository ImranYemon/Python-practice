# suggest an activity based on the weather (sunny-Go for a walk , rainy-read a book , snowy-make a snowman)

weather_input =  input("choose one \n sunny , rainy , snowy \n : ")

weather = weather_input.lower()

if weather == "sunny":
    activity ="Go for a walk"

elif weather == "rainy":
    activity ="read a book"

elif weather == "snowy" :
    activity ="make a snowman "

else :
    activity ="wrong entey"

print (activity)