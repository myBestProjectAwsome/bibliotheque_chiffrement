from .char_to_num import char_to_num
from .num_to_char import num_to_char

def encrypt_letter(letter,key):
    """chiffre une seule lettre avec la cle donnee"""

    x = char_to_num(letter)
    y = (x + key) % 26

    return num_to_char(y)

