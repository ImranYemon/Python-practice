# Print the multiplecation table for the given number upto 10 , but skip the 5th iteration . 

number = int(input("number : "))

for i in range (1 , 11) :
    if i == 5 :
        continue
    print(number , "X" , i , "=" , number*i)