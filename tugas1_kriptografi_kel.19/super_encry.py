# Function for the Vigenère Cipher encryption
def vigenere_encrypt(plaintext, key):
    key = key.upper()
    key_length = len(key)
    ciphertext = []

    for i in range(len(plaintext)):
        char = plaintext[i].upper()
        if char.isalpha():
            shift = ord(key[i % key_length]) - 65  # Calculate shift from the key
            encrypted_char = chr((ord(char) + shift - 65) % 26 + 65)  # Encrypt the character
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)  # Keep non-alphabetical characters unchanged

    return ''.join(ciphertext)

# Function for the Transposition Cipher encryption
def transposition_encrypt(text, key):
    key_length = len(key)
    num_columns = key_length
    num_rows = len(text) // key_length + (len(text) % key_length != 0)
    transposition_matrix = [''] * num_columns

    # Fill the matrix column-wise
    for i in range(len(text)):
        column = i % num_columns
        transposition_matrix[column] += text[i]

    # Rearrange based on the numeric order of the key
    key_order = sorted(list(key))
    ciphertext = ''
    for char in key_order:
        index = key.index(char)
        ciphertext += transposition_matrix[index]

    return ciphertext

# Combined Super Encryption (Vigenère + Transposition)
def super_encrypt(plaintext, vigenere_key, transposition_key):
    print("Original Plaintext:", plaintext)
    
    # First encrypt using the Vigenère Cipher
    vigenere_ciphertext = vigenere_encrypt(plaintext, vigenere_key)
    print("After Vigenère Cipher:", vigenere_ciphertext)
    
    # Then encrypt the result using the Transposition Cipher
    final_ciphertext = transposition_encrypt(vigenere_ciphertext, transposition_key)
    print("After Transposition Cipher:", final_ciphertext)
    
    return final_ciphertext

# Driver Code
def main():
    # Input plaintext and keys
    plaintext = input("Enter the plaintext: ").upper()
    vigenere_key = input("Enter the Vigenère Cipher key: ").upper()
    transposition_key = input("Enter the Transposition Cipher key: ").upper()

    # Perform super encryption
    ciphertext = super_encrypt(plaintext, vigenere_key, transposition_key)
    print("Super Encrypted Text:", ciphertext)

if __name__ == "__main__":
    main()
