import pytest
import sys
sys.path.insert(0, '..')
from src import encrypt
from src.brute_force import brute_force

class TestBruteForce:
    """tests pour l'attaque par force brute"""

    def test_retourne_26_resultats(self):
        """retourne exactement 26 resultats"""

        results = brute_force("KHOOR")
        assert len(results) == 26


    def test_structure_resultats(self):
        """chaque resultat contient key et tesxt"""

        results = brute_force("KHHOR")
        for r in results:
            assert "key" in r
            assert "text" in r

    def test_cle_0_a_25(self):
        """les cles vont de 0 a 25 dans lordre"""

        results = brute_force("KHOOR")

        keys = [r["key"] for r in results]
        assert keys == list(range(26))

    
    def test_trouve_message_original(self):
        """le bon message doit apparaitre dans les resultats"""

        # on chiffre HELLO avec la cle = 3 = KHOOR

        results = brute_force("KHOOR")
        texts = [r["text"] for r in results]
        assert "HELLO" in texts

    def test_bonne_cle(self):
        """le message original doit etre a la bonne cle"""
        res = brute_force("KHOOR")
        res_key_3 = res[3]
        assert res_key_3["key"] == 3
        assert res_key_3["text"] == "HELLO"

    
    def test_cle_zero_retourne_texte_identique(self):
        """avec cle 0 le texte ne change pas"""
        cipher = "KHOOR"
        results = brute_force(cipher)
        assert results[0]["text"] == cipher

    def test_avec_espaces_et_ponctuation(self):
        """les espaces et la ponctuation sont preserves"""
       
        results = brute_force("KHOOR ZRUOG!")
        result_key3 = results[3]
        assert result_key3["text"] == "HELLO WORLD!"

    def test_texte_vide(self):
        """un texte vide retourne 26 resultats vides"""
        results = brute_force("")
        assert len(results) == 26
        for r in results:
            assert r["text"] == ""

    def test_coherence_avec_encrypt(self):
        """pour toute cle k, brute_force retrouve le message original"""
        message = "BONJOUR MONDE"
        for key in range(26):
            cipher = encrypt(message, key)
            results = brute_force(cipher)
            assert results[key]["text"] == message