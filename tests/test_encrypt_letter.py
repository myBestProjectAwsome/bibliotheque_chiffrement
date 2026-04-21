import pytest

import sys
sys.path.insert(0, '..') 
from src import encrypt_letter


class TestEncryptLetter:
    """tests pour le chiffrements d'une lettre"""

    def test_cle_zero(self):
        """avec cle 0, la lettre ne change pas"""

        assert encrypt_letter('A',0) == 'A'
        assert encrypt_letter('M',0) == 'M'
        assert encrypt_letter('Z',0)== 'Z'

    def test_cesar_classique(self):
        """cesar avec cle 3 """
        assert encrypt_letter('A',3) == 'D'
        assert encrypt_letter('B',3) == 'E'
        assert encrypt_letter('C',3) == 'F'

    def test_bouclage_fin_alphabet(self):
        """Verifier le bouclage a la fin de l'alphabet"""

        assert encrypt_letter('X',3) == 'A'
        assert encrypt_letter('Y',3)== 'B'
        assert encrypt_letter('Z',3)== 'C'

    def test_rot13(self):
        """rot13:decalage de 13"""

        assert encrypt_letter('A',13)=='N'
        assert encrypt_letter('N',13) == 'A'

        def test_cle_25(self):
            """Clé 25 = reculer de 1"""
        assert encrypt_letter('A', 25) == 'Z'
        assert encrypt_letter('B', 25) == 'A'




