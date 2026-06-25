# write a function that greets a user . is no name is provided , it should greets with a defult name .

def greet(name = "user"):
    return "hello " + name + " !"

print(greet())
print(greet("Yemon"))
