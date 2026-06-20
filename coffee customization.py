# Order customization for coffee : "small", "medium", "large" with an option for "extra shot" of espresso. 

try :
    order_size_input = input("choose one \n small , meduim , large \n : ")
    order_size = order_size_input.lower()

    extra_shot_input = input("for extra shot press \n yes   no  \n :  ")
    extra_shot = extra_shot_input.lower()
    
    if extra_shot == "yes" :
        coffee = order_size + " espresso with extra shot" 
    else : 
        coffee = order_size + " espresso"

    print(coffee)

except :
    print("wrong entry")

