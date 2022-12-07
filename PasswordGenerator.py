import random

lcase_letter = "abcdefghijklmnopqrstuvwxyz"
ucase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = "$%&@!?*#"
numbers = "0123456789"

password = lcase_letter + ucase_letter + symbol + numbers
pass_len = int(input("Enter the length of the desired password: "))

generatedPass = "".join(random.sample(password, pass_len))

print("Your password is: ", generatedPass)
