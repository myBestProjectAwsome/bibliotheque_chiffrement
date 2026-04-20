import pytest

import sys
sys.path.insert(0, '..') 

from src.num_to_char import *


class TestNumToChar:
    """tests pour la conversion nombre -> lettre"""

    def test_zero(self):
        """0 doit donner A"""

        assert num_to_char(0) == 'A'

    def test_vingt_cinq(self):
        """25 doit donner Z"""
        assert num_to_char(25) == 'Z'

    def test_nombre_milieu(self):
        """12 doit donner M"""

        assert num_to_char(12) == 'M'

    def test_tous_les_nombres(self):
        """verifier tout les nombres de 0 a 25"""

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i in range(26):
            assert num_to_char(i) == alphabet[i]

            