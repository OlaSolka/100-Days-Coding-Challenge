# FizzBuzz
# If the number is divisible by 3 print Fizz
# If the number is divisible by 5 print Buzz
# If the number is divisible by 3 anf 5 print FizzBuzz

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n %3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
