from src import encrypt_letter
def encrypt(text,key):
    """chiffre un texte complet"""

    res = []

    for c in text:
        if c.isalpha():
            encrypted_char = encrypt_letter(c,key)
            res.append(encrypted_char)
        else:
            res.append(c)

    return ''.join(res)


