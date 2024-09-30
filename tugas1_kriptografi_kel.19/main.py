import vigenere_cipher.py
import auto_key_vigenere_cipher.py

def main():
    while True:
        print("Pilih metode enkripsi:")
        print("1. Vigenère Cipher")
        print("2. Auto-Key Vigenère Cipher")
        print("3. Keluar")

        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == '1':
            plaintext = input("Masukkan plaintext: ")
            key = input("Masukkan kunci: ")
            encrypted_text = vigenere_cipher.py.vigenere_encrypt(plaintext, key)
            print("Teks terenkripsi:", encrypted_text)
            decrypted_text = vigenere_cipher.py.vigenere_decrypt(encrypted_text, key)
            print("Teks terdekripsi:", decrypted_text)

        elif choice == '2':
            plaintext = input("Masukkan plaintext: ")
            auto_key = input("Masukkan kunci otomatis: ")
            encrypted_text = auto_key_vigenere_cipher.py.auto_key_encrypt(plaintext, auto_key)
            print("Teks terenkripsi:", encrypted_text)
            decrypted_text = auto_key_vigenere_cipher.py.auto_key_decrypt(encrypted_text, auto_key)
            print("Teks terdekripsi:", decrypted_text)

        elif choice == '3':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
