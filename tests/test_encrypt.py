import pytest
import sys
sys.path.insert(0, '..') 
from src import  encrypt


class TestEncrypt:
    """tests pour le chiffrement de textes"""


    def test_mot_simple(self):
        """chiffrer un mot simple"""
        assert encrypt("HELLO",3) == "KHOOR"

    
    def test_phrase_avec_espaces(self):
        """les espaces doivent etre conserves"""

        assert encrypt("HELLO WORLD",3) == "KHOOR ZRUOG"
        
    def test_avec_ponctuation(self):
        """la ponctuation doit etre conserves"""

        assert encrypt("BONJOUR!",5)== "GTSOTZW!"
        assert encrypt("A, B, C.",1)== "B, C, D."

    def test_minuscules_converties(self):
        """les minuscules doivent etre convertit en majuscules"""

        assert encrypt("hello", 3) == "KHOOR"
        assert encrypt("HeLLo", 3) == "KHOOR"
    
    def test_texte_vide(self):
        """un texte vide doit rester vide"""

        assert encrypt("",5) ==""

    def test_seulement_ponctuation(self):
        """Un texte sans lettres reste inchangé"""
        assert encrypt("123 !@# $%^", 10) == "123 !@# $%^"
    
    def test_alphabet_complet(self):
        """Chiffrer l'alphabet complet"""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = encrypt(alphabet, 1)
        assert result == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
    