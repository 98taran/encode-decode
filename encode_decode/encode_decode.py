def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            result += char  # keep spaces, punctuation, etc.
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Hey there! Welcome to your very own Secret Message Tool.")
    print("Here, you can ENCRYPT (hide) or DECRYPT (reveal) any message using a Caesar Cipher.")
    print("It's super simple — you just tell me your message and how much to shift the letters.\n")

    user_text = input("First, type the message you'd like me to process: ")

    while True:
        action = input("What would you like to do?\nType 'E' to Encrypt OR 'D' to Decrypt: ").strip().upper()
        if action in ['E', 'D']:
            break
        print("Oops! I didn’t catch that. Please enter 'E' or 'D'.")

    while True:
        try:
            shift = int(input("Now enter a number — this will be our secret shift amount (like 3 or 5): "))
            break
        except ValueError:
            print("That’s not a number! Please type a valid number.")

    if action == 'E':
        output = encrypt(user_text, shift)
        print("\nEncrypting your message...")
        print("Done! Here's your ENCRYPTED message:\n" + output)
    else:
        output = decrypt(user_text, shift)
        print("\nDecrypting your message...")
        print("Done! Here's your DECRYPTED message:\n" + output)

    print("\nThanks for using the Secret Message Tool. See you again!")

if __name__ == "__main__":
    main()
