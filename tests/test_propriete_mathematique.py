import pytest
import sys
sys.path.insert(0, '..') 
from src import  encrypt

class TestProprietesMathematiques:
    """tests des proprietes mathematiques du chiffrement"""

    def test_cle_26_identite(self):
        """cle 26 congrue cle 0 mod 26 : identite"""

        message = "HELLO"
        assert encrypt(message,0) == message.upper()

    def test_commutativite_cles(self):
        """encrypt(k1) puis encrypt(k2) = encrypt(k1+k2)"""
        message = "HELLO"
        k1, k2 = (3, 5)
        step1 = encrypt(message, k1)
        result1 = encrypt(step1, k2)
        result2 = encrypt(message, (k1 + k2) % 26)
        
        assert result1 == result2

    def test_inverse_additif(self):
        """encrypt(k) puis encrypt(26-k) redonne le message"""

        message = "HELLO WORLD"
        key = 7

        encrypted = encrypt(message,key)
        back = encrypt(encrypted,26 - key)

        assert back == message