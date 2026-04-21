import pytest
import sys
sys.path.insert(0, '..') 
from src import  decrypt
class TestDecrypt:
    """Tests pour le déchiffrement de textes"""
    
    def test_mot_simple(self):
        """Déchiffrer un mot simple"""
        assert decrypt("KHOOR", 3) == "HELLO"
    
    def test_phrase_avec_espaces(self):
        """Déchiffrer une phrase avec espaces"""
        assert decrypt("KHOOR ZRUOG", 3) == "HELLO WORLD"
    
    def test_avec_ponctuation(self):
        """Déchiffrer avec ponctuation"""
        assert decrypt("GTSOTZW!", 5) == "BONJOUR!"
    
    def test_texte_vide(self):
        """Un texte vide reste vide"""
        assert decrypt("", 5) == ""
