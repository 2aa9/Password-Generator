import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    """Generate a strong random password."""
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


if __name__ == "__main__":
    print("🔑 Password Generator 🔑")
    length = int(input("Enter password length (default 12): ") or 12)
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    pwd = generate_password(length, use_digits, use_symbols)
    print(f"\nGenerated password: {pwd}")
