# calculate the sume of even numbers ut to a given number N . 

number = int(input("number : "))
total = 0
for even_numbers in range(0,number) :
    if even_numbers % 2 == 0 :
        print(even_numbers)
        total += even_numbers
    
print(total)
