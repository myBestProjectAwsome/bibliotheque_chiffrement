import pytest
import sys
sys.path.insert(0, '..') 
from src import decrypt_letter,encrypt_letter

class TestDecryptLetter:
    """test pour le dechiffrement d une lettre"""

    def test_cle_zero(self):
        """avec la cle 0, la lettre ne change pas"""

        assert decrypt_letter('A',0) == 'A'
        assert decrypt_letter('M',0) == 'M'

    def test_cesar_classique(self):
        """dechiffrer avec cle 3"""

        assert decrypt_letter('D',3) == 'A'
        assert decrypt_letter('E',3) == 'B'

    
    def test_bouclage_debut_alphabet(self):
        """verifier le bouclage au debut de l'alphabet"""

        assert decrypt_letter('A',3) == 'X'
        assert decrypt_letter('B',3) == 'Y'
        assert decrypt_letter('C',3) == 'Z'

    def test_inverse_encrypt(self):
        """decrypt(encrypt(x)) = x pour une lettre"""

        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for key in range(26):
                encrypted = encrypt_letter(letter,key)
                decrypted = decrypt_letter(encrypted,key)
                assert decrypted == letter