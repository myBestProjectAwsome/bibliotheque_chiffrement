import char_to_num
import num_to_char
import encrypt_letter
import decrypt_letter
import encrypt
import decrypt


if __name__ == '__main__':
    # message a chiffrer 

    message = "BONJOUR MONDE"

    key = 3

    print("=== chiffrement de cesar ====")

    print(f"message original : {message}"
          )
    
    print(f"cle de decalage : {key}")

    # chiffrement 
    encrypted = encrypt.encrypt(message,key)
    print(f"Message chiffré  : {encrypted}")
    print()
    # dechiffrement
    decrypted = decrypt.decrypt(encrypted, key)
    print(f"Message déchiffré: {decrypted}")
    print()

    # verification 

    if message == decrypted:
        print("Le déchiffrement est correct !")
    else:
        print("Erreur de déchiffrement")