def encrypt(plaintext, shift):
   # Encrypts the given plaintext using the Caesar Cipher.

    #Parameters:
     #   plaintext (str): The text to be encrypted.
      #  shift (int): The number of positions each letter will be shifted.

    #Returns:
    #    str: The encrypted text.
    shift = int(shift) 
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

def decrypt(ciphertext, shift):

    #Decrypts the given ciphertext using the Caesar Cipher.

   # Parameters:
     #   ciphertext (str): The text to be decrypted.
    #    shift (int): The number of positions that were used to shift the original text.

    #Returns:
        #str: The decrypted text.
    # Decrypting is the reverse of encrypting: use the negative of the original shift.
    return encrypt(ciphertext, -int(shift))