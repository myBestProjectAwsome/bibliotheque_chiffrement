import pytest

import sys
sys.path.insert(0, '..') 

from src import *

class TestCasLimites:
    """tests de cas limites et edges cases"""

    def test_une_seule_lettre(self):
        """texte d'une seule lettre"""

        assert encrypt("A",5) == "F"
        assert decrypt("F",5) == "A"

    
    def test_texte_tres_long(self):
        """verifier que sa marche avec un texte long"""

        message = "A"  * 1000
        encrypted = encrypt(message,13)
        decrypted = decrypt(encrypted,13)
        assert decrypted == message

    def test_tous_les_caracteres_speciaux(self):
        """Caractères spéciaux divers"""
        message = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        assert encrypt(message, 5) == message
    
    def test_chiffres(self):
        """Les chiffres doivent être conservés"""
        message = "ABC 123 XYZ"
        result = encrypt(message, 3)
        assert "123" in result