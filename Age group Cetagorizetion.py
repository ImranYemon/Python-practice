# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).


age = int(input("Input your age : "))

if age>120:
    print("Wrong entry\n you have entered more then age limit number  ")
    
    exit()
try:

    if age<=13:
        print("Child")
    elif age>=13 and age<=19 : 
        print("Teenager")
    elif age>=19 and age<=59 :
        print("Adult")
    elif age>=60 : 
        print("senior")
    else :
        print("please input properly")

except:
    print("please input any number")
