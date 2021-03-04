name = input("What is your name?")
print("The name you entered was", name)
greeting = "How old are you, "+name+"?"
age = input(greeting)
year = 2021 - int(age)
print(name, ", you were born in:", year)