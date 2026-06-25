# Check if a password is "week" "strong" or "medium" criteria (charecter<6 "week" , charecter>6<10 "medium" , charecter >10 "strong")

password = input ("input password : ")

if len(password)<=6 :
    print("week")
elif len(password)>6 and len(password)<=10 :
    print("medium")
else :
    print("strong")