import random
import string
from datetime import datetime

def greet_user():
    print("🔐 Welcome to Smart Password Generator!")
    name = input("Enter your name: ").strip()
    dob = input("Enter your date of birth (YYYY-MM-DD): ").strip()
    return name, dob

def get_complexity():
    print("\nPassword Complexity Options:")
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    return use_upper, use_digits, use_symbols

def build_char_pool(use_upper, use_digits, use_symbols):
    chars = list(string.ascii_lowercase)
    if use_upper:
        chars += list(string.ascii_uppercase)
    if use_digits:
        chars += list(string.digits)
    if use_symbols:
        chars += list("!@#$%^&*()_-+=<>?")
    return chars

def create_personal_prefix(name, dob):
    initials = ''.join([part[0] for part in name.split() if part])
    try:
        dob_obj = datetime.strptime(dob, "%Y-%m-%d")
        dob_part = dob_obj.strftime("%d%m")  # Day and Month
    except:
        dob_part = "0000"  # fallback if DOB format is wrong
    return initials + dob_part

def generate_password(length, chars, prefix=""):
    if length < len(prefix) + 4:
        print(f"Password too short for personal prefix. Minimum length: {len(prefix)+4}")
        return None
    random_part = ''.join(random.choice(chars) for _ in range(length - len(prefix)))
    password = prefix + random_part
    return ''.join(random.sample(password, len(password)))  # shuffle for extra randomness

def main():
    name, dob = greet_user()
    try:
        length = int(input("Enter desired password length (min 8): "))
        if length < 8:
            print("Password length should be at least 8.")
            return
    except ValueError:
        print("Invalid input for length.")
        return

    use_upper, use_digits, use_symbols = get_complexity()
    chars = build_char_pool(use_upper, use_digits, use_symbols)

    prefix = create_personal_prefix(name, dob)
    password = generate_password(length, chars, prefix)

    if password:
        print("\n✅ Your personalized strong password is:")
        print(f"👉 {password}")
        print("\nPassword includes:")
        print("- Initials + DOB snippet for personal touch")
        if use_upper: print("- Uppercase letters")
        if use_digits: print("- Numbers")
        if use_symbols: print("- Symbols")
        print("🔁 Randomized for strong security!")

if __name__ == "__main__":
    main()
