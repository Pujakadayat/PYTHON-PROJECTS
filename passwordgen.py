import random
import string

# def password(min_length,numbers=True,special_characters = True):
#     letters =string.ascii_letters
#     digits = string.digits
#     special= string.punctuation
    
#     characters = letters
#     if numbers:
#         characters+=digits
#     if special_characters:
#         characters+=special
        
#     pwd= ""
#     meets_criteria=False
#     has_number = False
#     has_special =False
    
#     while not meets_criteria or len(pwd) < min_length:
#         new_char = random.choice(characters)
#         pwd +=new_char
        
#         if new_char in digits:
#             has_number=True
#         elif new_char in special:
#              has_special=True
             
#         meets_criteria = True
#         if numbers:
#             meets_criteria = has_number
#         if special_characters:
#             meets_criteria =  meets_criteria and has_special
            
            
#     return pwd 
 
# min_length = int(input("enter the min password length") ) 
# has_number = input("do you want to have numbers? y/n").lower() == 'y'
# has_special = input("do you want to have special characters? y/n") .lower() == 'y' 
# pwd = password(min_length,has_number,has_special)

# print("The generated password is :" , pwd)



def passwords(min_length, has_letters=True, has_number=True, has_special=True):

    print("Welcome to password generator")
    characters = ""
    
    if has_letters:
        characters += string.ascii_letters
    if has_number:
        characters += string.digits
    if has_special:
        characters+=string.punctuation
    return characters



 
min_length = int(input("enter the min password length") ) 
has_number = input("do you want to have numbers? y/n").lower() == 'y'
has_special = input("do you want to have special characters? y/n") .lower() == 'y'  or "n"
has_letters = input ("do you want to have letters?(Y/N)") == 'y'

characters = passwords(min_length, has_letters, has_number, has_special)
password = ''.join(random.choice(characters) for _ in range(min_length))

print("The generated password is :" , password)

            
        