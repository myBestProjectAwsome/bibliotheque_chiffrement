import pytest

import sys
sys.path.insert(0, '..') 

from src.char_to_num import *
from src.num_to_char import *

class TestBijection:
    """tests pour verifier que chartonum et numtochar sont inverses"""

    def test_lettre_nombre_lettre(self):
        """lettre->nombre->lettre doit redonner la lettre originale"""

        for k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            n = char_to_num(k)
            res = num_to_char(n)
            assert res == k 


    def test_nombre_lettre_nombre(self):
        """nombre ->lettre -> nombre doit redonner le nombre original"""

        for n in range(26):
            letter = num_to_char(n)
            res = char_to_num(letter)
            assert res == n