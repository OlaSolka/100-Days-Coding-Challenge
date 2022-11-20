import random
print("Welcome to \"Who will pay today?\" generator!")

names_str = input("Give everybody's name separated by a coma: ")

names = names_str.split(", ")

# members = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

print(names)
for i in range(1):
    print(random.choice(names))
