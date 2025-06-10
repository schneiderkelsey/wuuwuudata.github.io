name = input("What's your name? /n")

with open('example.txt', 'w') as file:
    file.write(f"{name} created this file") 
    
color = input("What's your favorite color? /n")

with open('example.txt', 'w') as file:
    file.write(f"{color} is your favorite color") 