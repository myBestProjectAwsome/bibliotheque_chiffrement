def num_to_char(n):
    """convertit un nombre en lettre"""

    return chr(n+ord('A'))

# jeux de tests

print(num_to_char(0))
print(num_to_char(1))
print(num_to_char(25))
print(num_to_char(7))