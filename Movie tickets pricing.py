# Movie tickets pricing are based on age , 12$ for adults(over 18) 8$ for children . Everyone gets a 2$ discount on wednesday. 

age = int(input("Your age : "))

day = input("Day : ")

price = 12 if age >= 18 else 8 

if day == "wednesday" :  
    price = price - 2 

print(price)
