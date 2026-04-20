from .decrypt_letter import decrypt_letter


def decrypt(text,key):
    """dechiffre un texte complet"""


    res = []

    for c in text:
        if c.isalpha():
            decrypted_char = decrypt_letter(c,key)
            res.append(decrypted_char)
        else:
            res.append(c)

    return ''.join(res)


# jeux de tests

print(decrypt("KHOOR",3))
print(decrypt("BCD",1))
print(decrypt("ABC",3))
print(decrypt("GTSOTZW !",5))