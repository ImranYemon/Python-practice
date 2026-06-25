#  Keep asking the user for input until they enter a number between 1 to 10 . 


while True :
    user_input = int(input("input : "))
    if 1 <= user_input <= 10 :
        print ("validate") 
        break
    else: 
        print("invalid , try again !")