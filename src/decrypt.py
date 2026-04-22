from src import decrypt_letter


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


