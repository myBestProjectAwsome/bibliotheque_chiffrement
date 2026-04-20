import pytest
import sys
sys.path.insert(0, '..') 

from src.char_to_num import *
class TestCharToNum:
    """tests pour la conversion lettre -> nombre"""

    def test_premiere_lettre(self):
        """renvoie true ; sinon false"""

        assert char_to_num('A') == 0

    def test_derniere_lettre(self):
        """test la derniere lettre"""

        assert char_to_num('Z') == 25

    def test_lettre_milieu(self):
        """M doit donner 12"""

        assert char_to_num('M') == 12

    
    def test_minuscule(self):
        """verifie si les minuscules sont convertit en majuscules"""

        assert char_to_num('a') == 0
        assert char_to_num('z') == 25

    def test_toutes_les_lettres(self):
        """on verifie toutes les lettres de A a Z"""

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for k,letter in enumerate(alphabet):
            assert char_to_num(letter) == k



