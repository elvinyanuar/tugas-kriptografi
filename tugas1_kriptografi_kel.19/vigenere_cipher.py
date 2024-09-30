def vigenere_encrypt(plaintext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    keyword_repeated = ""

    # Ulangi kata kunci agar panjangnya sama dengan plaintext
    j = 0
    for i in range(len(plaintext)):
        if plaintext[i].upper() in alphabet:
            keyword_repeated += keyword[j % len(keyword)].upper()
            j += 1
        else:
            keyword_repeated += plaintext[i]  # Tambahkan karakter non-alfabet tanpa mengubah

    # Enkripsi
    for i in range(len(plaintext)):
        if plaintext[i].upper() in alphabet:
            plaintext_index = alphabet.index(plaintext[i].upper())
            keyword_index = alphabet.index(keyword_repeated[i])
            encrypted_index = (plaintext_index + keyword_index) % 26
            ciphertext += alphabet[encrypted_index]
        else:
            ciphertext += plaintext[i]  # Tambahkan karakter non-alfabet tanpa mengubah

    return ciphertext

def vigenere_decrypt(ciphertext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = ""
    keyword_repeated = ""

    # Ulangi kata kunci agar panjangnya sama dengan ciphertext
    j = 0
    for i in range(len(ciphertext)):
        if ciphertext[i].upper() in alphabet:
            keyword_repeated += keyword[j % len(keyword)].upper()
            j += 1
        else:
            keyword_repeated += ciphertext[i]  # Tambahkan karakter non-alfabet tanpa mengubah

    # Dekripsi
    for i in range(len(ciphertext)):
        if ciphertext[i].upper() in alphabet:
            ciphertext_index = alphabet.index(ciphertext[i].upper())
            keyword_index = alphabet.index(keyword_repeated[i])
            decrypted_index = (ciphertext_index - keyword_index) % 26
            decrypted_text += alphabet[decrypted_index]
        else:
            decrypted_text += ciphertext[i]  # Tambahkan karakter non-alfabet tanpa mengubah

    return decrypted_text

# Meminta input dari pengguna
plaintext = input("Masukkan plaintext: ")
keyword = input("Masukkan keyword: ")

# Menghapus spasi dan mengubah ke huruf kapital
plaintext = plaintext.replace(" ", "").upper()
keyword = keyword.replace(" ", "").upper()

# Enkripsi dan Dekripsi
ciphertext = vigenere_encrypt(plaintext, keyword)
decrypted_text = vigenere_decrypt(ciphertext, keyword)

# Menampilkan hasil
print(f"\nPlaintext: {plaintext}")
print(f"Keyword: {keyword}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted_text}")
