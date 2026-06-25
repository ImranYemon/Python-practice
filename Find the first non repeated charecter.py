# Given a string , find the first non-repeated charecter . 

input_string = input("input string : ")

for charecter in input_string :
    if input_string.count(charecter) == 1 :
        print("the first non-repeated charecter is : " , charecter)
        break