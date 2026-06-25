# check all elements in the list is unique . if a duplicate found exit the loop and find the element.

items = ["apple" , "banana" , "oringe" , "mango" , "mango"]
unique_item = set()

for item in items :
    if item in unique_item :
        print ("duplicate" , item)
        break
    else :
        unique_item.add(item)
