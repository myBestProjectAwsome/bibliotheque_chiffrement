from .char_to_num import char_to_num
from .num_to_char import num_to_char

def decrypt_letter(letter,key):

    """dechiffre une seule lettre"""


    y = char_to_num(letter)

    x = (y-key) %26

    return num_to_char(x)


