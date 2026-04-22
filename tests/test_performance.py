import pytest

import sys
sys.path.insert(0, '..') 

from src import encrypt


class TestPerformance:
    """Tests de performance basiques"""
    
    def test_temps_execution_acceptable(self):
        """Le chiffrement doit être rapide"""
        import time
        
        message = "A" * 10000  
        key = 13
        
        start = time.time()
        encrypted = encrypt(message, key)
        duration = time.time() - start
        
        assert duration < 0.1