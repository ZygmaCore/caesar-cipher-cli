import os
from module import *

start = input("Press Enter to Start ")
while start == "":
    logo()
    picking = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if picking == "encode":
        message = input("Type your message:\n")
        shift_number = int(input("Type the shift number:\n"))

        result = ""
        for iteration in message:
            if iteration in alphabet:
                x = alphabet.index(iteration)
                new_index = (x + shift_number) % 26
                result += alphabet[new_index]
            else:
                result += iteration

        print(f"Here's the encoded result: {result}")
        again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
        if again == "yes":
            os.system("clear")
        else:
            break

    elif picking == "decode":
        message = input("Type your message:\n")
        shift_number = int(input("Type the shift number:\n"))

        result = ""
        for iteration in message:
            if iteration in alphabet:
                x = alphabet.index(iteration)
                new_index = (x - shift_number) % 26
                result += alphabet[new_index]
            else:
                result += iteration

        print(f"Here's the decoded result: {result}")
        again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
        if again == "yes":
            os.system("clear")
        else:
            break
    else:
        print("Only Encode and Decode Available ")
        break

print("Have a Nice Day!")
