from logo import logo
print(logo)
print("Hello! Welcome to thee caesar cipher!\nWhat do you want to do?")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end_of_cipher = False
while not end_of_cipher:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))
    shift = shift_input % 26


    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for i in start_text:
            if i in alphabet:
                position = alphabet.index(i)
                new_position = position+shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += i
        print(f"Your {cipher_direction}d text is {end_text}")


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    decision = input("Do you want to use caesar cipher again? Type \"yes\" or \"no\"").lower()
    if decision == "no":
        end_of_cipher = True
        print("Goodbye!")


