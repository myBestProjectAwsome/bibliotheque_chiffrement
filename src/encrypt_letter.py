import char_to_num
import num_to_char

def encrypt_letter(letter,key):
    """chiffre une seule lettre avec la cle donnee"""

    x = char_to_num.char_to_num(letter)
    y = (x + key) % 26

    return num_to_char.num_to_char(y)

# jeux de tests

print(encrypt_letter('A',3))
print(encrypt_letter('X',3))
print(encrypt_letter('H',3))