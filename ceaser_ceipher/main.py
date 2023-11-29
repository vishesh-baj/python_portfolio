print("Welcome to Caesar Cipher")


def cipher(cipher_type, message, shift_number):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                     'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                     's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ciphered_value = message

    if cipher_type == "encode":
        encoded_message = ""
        for letter_index in range(0, len(message)):
            for alphabet_index in range(0, len(alphabet_list)):
                if alphabet_list[alphabet_index] == ciphered_value[letter_index]:
                    shifted_letter = alphabet_list[(alphabet_index + shift_number) % len(alphabet_list)]
                    encoded_message += shifted_letter
        print("Encoded String: ", encoded_message)

    elif cipher_type == "decode":
        decoded_message = ""
        for letter_index in range(0, len(message)):
            for alphabet_index in range(0, len(alphabet_list)):
                if alphabet_list[alphabet_index] == ciphered_value[letter_index]:
                    shifted_letter = alphabet_list[(alphabet_index - shift_number) % len(alphabet_list)]
                    decoded_message += shifted_letter
        print("Decoded String: ", decoded_message)


iterator = True

while iterator:
    cipher_type_value = input("What do you want to achieve? encrypt or decode: ")
    cipher_message = input("Enter a message to cipher: ")
    cipher_shift_number = int(input("Enter shift number: "))

    cipher(cipher_type_value, cipher_message, cipher_shift_number)

    continue_loop = input("Would you like to continue or exit? Enter 'yes' to continue, and 'no' to terminate: ")
    if continue_loop.lower() == "no":
        iterator = False
