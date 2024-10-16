import random
import string

def get_correct_number(num):
    while True:
        try:
            value = int(input(num))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Incorrect input. Please enter a number.")

def get_correct_inp(inp):
    while True:
        inp_str = input(inp).strip().lower()
        if inp_str in ["y", "n"]:
            return inp_str == "y"
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def replace_lett_to_numb(passwodr):
    replacements = {'i': '1', 'f': '4', 'o': '0', 's': '5'} #хочу заменять только строчные, хотя можно сделать и то, и то
    for lett, numb in replacements.items():
        passwodr = passwodr.replace(lett, numb)
    return passwodr

def generate_passwords(lenght, use_upp, use_digits, use_special, replace_chars):
    characters = string.ascii_lowercase

    if use_upp:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(lenght))

    if replace_chars:
        password = replace_lett_to_numb(password)

    return password

num_of_pass = get_correct_number("How many passwords do you need? ")
pass_length = get_correct_number("How many characters is the password length? ")
use_upp = get_correct_inp("Should I include a different case of characters (y/n)? ")
use_digits = get_correct_inp("Include numbers (y/n)? ")
use_special = get_correct_inp("Should I include special characters (y/n)? ")
replace_chars = get_correct_inp("Replace some letters with numbers (y/n)? ")

print("Your passwords:")
for _ in range(num_of_pass):
    print(generate_passwords(pass_length, use_upp, use_digits, use_special, replace_chars))
