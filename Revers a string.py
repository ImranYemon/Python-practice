#  Reverse a string using a loop . 
input_string = input("input string : ")
reversed_String = ""

for charecter in input_string :
    reversed_String = charecter + reversed_String

print(reversed_String)