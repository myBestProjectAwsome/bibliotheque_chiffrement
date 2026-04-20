def char_to_num(c):
    """Convertit une lettre en nombre"""

    return ord(c.upper()) - ord('A')

# tests unitaires


print(char_to_num('A'))
print(char_to_num('B'))
print(char_to_num('Z'))
print(char_to_num('h'))