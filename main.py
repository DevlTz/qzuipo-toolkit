from ciphers import caesar, vigenere
from utils.text_utils import validate_input, clean_text, print_result

CIPHERS = {
    'caesar': caesar,
    'vigenere': vigenere,
}

def main():
    while True:
        cipher_type = input("\nCipher type (caesar/vigenere): ").lower()
        if cipher_type not in CIPHERS:
            print("Not supported yet."); continue

        text = clean_text(input("Text: "))
        key  = input("Key: ")

        try:
            validate_input(text, key)
        except ValueError as e:
            print(e); continue

        op = input("(E)ncrypt or (D)ecrypt? ").upper()
        module = CIPHERS[cipher_type]

        if op == 'E':
            result = module.encrypt(text, key)
            print_result("ENCRYPTED", text, result)
        elif op == 'D':
            result = module.decrypt(text, key)
            print_result("DECRYPTED", text, result)

        again = input("\nAnother operation? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    main()