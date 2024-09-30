# Python program to implement Playfair Cipher with encryption and decryption

# Function to convert the string to lowercase
def toLowerCase(text):
    return text.lower()

# Function to remove all spaces in a string
def removeSpaces(text):
    return ''.join(text.split())

# Function to group 2 elements of a string as a list element
def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
        group = i
    Diagraph.append(text[group:])
    return Diagraph

# Function to fill a letter in a string element if 2 letters in the same string matches
def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + 'x' + text[i+1:]
                return FillerLetter(new_word)
        return text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + 'x' + text[i+1:]
                return FillerLetter(new_word)
        return text

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to generate the 5x5 key square matrix
def generateKeyTable(key, list1):
    key_letters = []
    for i in key:
        if i not in key_letters:
            key_letters.append(i)

    matrix = []
    compElements = key_letters + [i for i in list1 if i not in key_letters]
    
    while compElements:
        matrix.append(compElements[:5])
        compElements = compElements[5:]
    
    return matrix

def search(mat, element):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == element:
                return i, j

# Encrypt Row Rule
def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    return matr[e1r][(e1c + 1) % 5], matr[e2r][(e2c + 1) % 5]

# Decrypt Row Rule
def decrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    return matr[e1r][(e1c - 1) % 5], matr[e2r][(e2c - 1) % 5]

# Encrypt Column Rule
def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    return matr[(e1r + 1) % 5][e1c], matr[(e2r + 1) % 5][e2c]

# Decrypt Column Rule
def decrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    return matr[(e1r - 1) % 5][e1c], matr[(e2r - 1) % 5][e2c]

# Encrypt Rectangle Rule
def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    return matr[e1r][e2c], matr[e2r][e1c]

# Decrypt Rectangle Rule (same as encryption)
def decrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    return matr[e1r][e2c], matr[e2r][e1c]

# Function to encrypt the plaintext
def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(len(plainList)):
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        CipherText.append(c1 + c2)
    return ''.join(CipherText)

# Function to decrypt the ciphertext
def decryptByPlayfairCipher(Matrix, cipherList):
    PlainText = []
    for i in range(len(cipherList)):
        ele1_x, ele1_y = search(Matrix, cipherList[i][0])
        ele2_x, ele2_y = search(Matrix, cipherList[i][1])

        if ele1_x == ele2_x:
            p1, p2 = decrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            p1, p2 = decrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            p1, p2 = decrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        PlainText.append(p1 + p2)
    return ''.join(PlainText)

# Main function to run encryption and decryption
def main():
    text_Plain = input("Enter the plaintext: ").lower()
    text_Plain = removeSpaces(text_Plain)
    PlainTextList = Diagraph(FillerLetter(text_Plain))
    if len(PlainTextList[-1]) != 2:
        PlainTextList[-1] = PlainTextList[-1] + 'z'

    key = input("Enter the key: ").lower()
    Matrix = generateKeyTable(key, list1)

    # Encrypt the plaintext
    cipherText = encryptByPlayfairCipher(Matrix, PlainTextList)
    print("Ciphertext:", cipherText)

    # Prepare ciphertext for decryption
    cipherList = Diagraph(cipherText)

    # Decrypt the ciphertext
    decryptedText = decryptByPlayfairCipher(Matrix, cipherList)
    print("Decrypted text:", decryptedText)

if __name__ == "__main__":
    main()
