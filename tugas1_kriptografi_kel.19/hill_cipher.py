# Python3 code to implement Hill Cipher with user input for message and key (Encryption and Decryption)

import numpy as np

# Initialize keyMatrix (3x3 matrix)
keyMatrix = np.zeros((3, 3), dtype=int)

# Generate vector for the message
messageVector = np.zeros((3, 1), dtype=int)

# Generate vector for the cipher
cipherMatrix = np.zeros((3, 1), dtype=int)

# Function to generate the key matrix from the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Function to encrypt the message
def encrypt(messageVector):
    global cipherMatrix
    cipherMatrix = np.dot(keyMatrix, messageVector) % 26

# Function to find the modular inverse of a matrix
def modInverseMatrix(matrix):
    det = int(np.round(np.linalg.det(matrix)))  # Determinant
    det_inv = pow(det, -1, 26)  # Modular inverse of the determinant
    adjugate_matrix = np.round(np.linalg.inv(matrix) * det).astype(int)  # Adjugate matrix
    inv_matrix = (det_inv * adjugate_matrix) % 26
    return inv_matrix

# Function to decrypt the ciphertext
def decrypt(cipherMatrix, keyMatrix):
    inverseKeyMatrix = modInverseMatrix(keyMatrix)
    decryptedMatrix = np.dot(inverseKeyMatrix, cipherMatrix) % 26
    return decryptedMatrix

# Function to perform the Hill Cipher encryption and decryption
def HillCipher(message, key, decrypt_mode=False):
    # Get key matrix from the key string
    getKeyMatrix(key)

    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

    if not decrypt_mode:
        # Encryption
        encrypt(messageVector)
        CipherText = [chr(int(cipherMatrix[i][0]) + 65) for i in range(3)]
        print("Ciphertext: ", "".join(CipherText))
    else:
        # Decryption
        decryptedMatrix = decrypt(messageVector, keyMatrix)
        PlainText = [chr(int(decryptedMatrix[i][0]) + 65) for i in range(3)]
        print("Decrypted text: ", "".join(PlainText))

# Driver Code
def main():
    mode = input("Enter mode (encrypt/decrypt): ").lower()
    message = input("Enter the message (3 characters): ").upper()
    key = input("Enter the key (9 characters): ").upper()

    # Ensure that the inputs are valid
    if len(message) != 3:
        print("Error: The message must be exactly 3 characters long.")
        return
    if len(key) != 9:
        print("Error: The key must be exactly 9 characters long.")
        return

    if mode == "encrypt":
        HillCipher(message, key)
    elif mode == "decrypt":
        HillCipher(message, key, decrypt_mode=True)
    else:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
