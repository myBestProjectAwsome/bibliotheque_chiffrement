import char_to_num
import num_to_char

def decrypt_letter(letter,key):

    """dechiffre une seule lettre"""


    y = char_to_num.char_to_num(letter)

    x = (y-key) %26

    return num_to_char.num_to_char(x)


# jeux de tests

print(decrypt_letter('D',3))
print(decrypt_letter('A',3))
print(decrypt_letter('K',3))