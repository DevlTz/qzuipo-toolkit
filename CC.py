# Welcome message that describes the historical context and concept of the Caesar Cipher.
welcome_message = (
    "Cryptography's history is long, dating back to ancient Egypt in 1900 BCE. "
    "One of the simplest historical ciphers is the Caesar Cipher from the first century BCE. "
    "The concept is straightforward: shift each letter by a certain number to encrypt the message."
)

# Message displayed when no input is provided.
empty_message = "No input provided."

def display_welcome():
    # Displays the welcome message to the user.

    print(welcome_message)

def caesar_cipher_encrypt(plaintext, shift):
   # Encrypts the given plaintext using the Caesar Cipher.
    
    #Parameters:
     #   plaintext (str): The text to be encrypted.
      #  shift (int): The number of positions each letter will be shifted.
    
    #Returns:
    #    str: The encrypted text.
    
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            # Determine the base ASCII code based on whether the character is uppercase or lowercase
            shift_base = ord('A') if char.isupper() else ord('a')
            # Calculate the new character after applying the shift,
            # using modulo 26 to wrap around the alphabet.
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            # Leave non-alphabetic characters unchanged.
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):

    #Decrypts the given ciphertext using the Caesar Cipher.
    
   # Parameters:
     #   ciphertext (str): The text to be decrypted.
    #    shift (int): The number of positions that were used to shift the original text.
    
    #Returns:
        #str: The decrypted text.
    # Decrypting is the reverse of encrypting: use the negative of the original shift.
    return caesar_cipher_encrypt(ciphertext, -shift)

def main():

    #Main function that runs the cipher application.
    #It prompts the user to choose between encryption and decryption, then processes the input accordingly.

    # Display the welcome message.
    display_welcome()
   
    # Select the Cryptograph Type

    # /////// --------------------------------> Updates tomorrow <------------------------------ //////
    # print ("\n Type a Cryptograpth Type:")
    # if option not in [types]:
    #   print("Sorry, we don't have support for this Type yet")
    #   return




     # Present the user with options to either encrypt or decrypt text.
    print("\nSelect an option:")
    print("1. Encrypt text using the Caesar Cipher")
    print("2. Decrypt text using the Caesar Cipher")
    
    # Read the user's choice.
    option = input("Enter the number corresponding to your choice: ")
    
    # Validate the user's choice.
    if option not in ['1', '2']:
        print("Invalid option selected. Please restart the program and choose either 1 or 2.")
        return
    

    # Prompt the user to enter the text.
    text = input("\nEnter the text: ")
    if not text:
        print(empty_message)
        return
    
    # Prompt the user to enter the shift key and handle invalid inputs.
    try:
        shift = int(input("Enter the key (an integer) for the shift: "))
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return
    # Process the text based on the selected option.
    if option == '1':
        # Encrypt the text.
        result = caesar_cipher_encrypt(text, shift)
        print("\nEncrypted text:", result)
    elif option == '2':
        # Decrypt the text.
        result = caesar_cipher_decrypt(text, shift)
        print("\nDecrypted text:", result)

# Entry point of the script.
if __name__ == "__main__":
    main()

