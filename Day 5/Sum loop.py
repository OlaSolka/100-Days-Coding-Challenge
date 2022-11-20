# range fron 1 to 100
# sum all of the even numbers

total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total = total + number
print(total)