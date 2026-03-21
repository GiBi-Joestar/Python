# collect user preferences
# - length
# - should contain uppercase
# - should contain lowercase
# - should contain digits


# - get all available characters
# - randomly pick characters up to length
# - ensure we have at least one of each character type
# - ensure length is valid


import random
import string

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppsercase letters?: ").strip().lower()
    include_special = input("Include special characters?: ").strip().lower()
    include_digits = input("Include digits?: ").strip().lower()


    if length < 4 :
        print("Password lengthmust be at least 4 characters")
        return
    
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else  ""
    special = string.punctuation if include_special == "yes" else  ""
    digits = string.digits if include_digits == "yes" else  ""

    all_characters = lower + uppercase + special + digits

    required_caracters = []
    if include_uppercase == "yes":
        required_caracters.append(random.choice(uppercase))
    if include_special == "yes":
        required_caracters.append(random.choice(special))
    if include_digits == "yes":
        required_caracters.append(random.choice(digits))

    remaining_length = length -  len(required_caracters)
    password = required_caracters


    for _ in range(remaining_length):
        characters = random.choice(all_characters)
        password.append(characters)


    random.shuffle(password)
    str_password = "".join(password)
    return str_password

password = generate_password()
print(password)