# Choose a mode of transport based on distance (if , <3 "walk" >3-15 "bike" >15 "car")

try :
        
    Distance = int(input("enter distance : "))

    if Distance <= 3 :
        transport = "walk"

    elif Distance >= 3 and Distance < 15 :
        transport = "bike"

    elif Distance >=15 :
        transport = "car"
    else :
        print ("wrong entry")

    print(transport)

except:
    print("wrong entry")