import pytest
import sys
sys.path.insert(0, '..') 
from src import  decrypt,encrypt

class TestRoundTrip:
    """Tests de réversibilité : encrypt puis decrypt"""
    
    def test_hello_world(self):
        """Test classique"""
        message = "HELLO WORLD"
        key = 3
        encrypted = encrypt(message, key)
        decrypted = decrypt(encrypted, key)
        assert decrypted == message
    
    def test_toutes_les_cles(self):
        """Vérifier pour toutes les clés possibles"""
        message = "TEST MESSAGE"
        for key in range(26):
            encrypted = encrypt(message, key)
            decrypted = decrypt(encrypted, key)
            assert decrypted == message

    def test_texte_long(self):
        """test avec un texte plus long"""

        message = "CECI EST UN MESSAGE SECRET AVEC PONCTUATION !"

        key = 7
        encrypted = encrypt(message,key)
        decrypted = decrypt(encrypted,key)
        assert decrypted == message

    def test_alphabet_complet(self):
        """test avec toutes les lettres"""
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for key in range(26):
            encrypted = encrypt(message, key)
            decrypted = decrypt(encrypted, key)
            assert decrypted == message
        
