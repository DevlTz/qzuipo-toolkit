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

def select_option():
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


# def get_text(text):


def main():

    #Main function that runs the cipher application.
    #It prompts the user to choose between encryption and decryption, then processes the input accordingly.

    # Display the welcome message.
    display_welcome()

    # Select the Cryptograph Type

    # /////// --------------------------------> Updates tomorrow <------------------------------ //////
    types = input("\n Type a Cryptograpth Type: ")

    if types == 'Caesar':
     return select_option(Caesar) 

    #elif types == 'Vignnere':

    elif option not in [types]:
       print("Sorry, we don't have support for this Type yet")
       return

     # Present the user with options to either encrypt or decrypt text.
   # Entry point of the script.
if __name__ == "__main__":
    main()




#Things that need to be in there.

# -> After Decrypt - Consider if the user want to encrypt another thing
# -> Try brute force or consistent decrypt this
# -> Vignere Cipher
# -> Hash 256
# -> Better Interface
# -> Credits on sublines
# -> Install dependencies alone
# - > Improve the crypt system.
