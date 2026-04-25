"""analyse frequentielle pour casser le chiffrement de cesar

principe : 

  en francais, la lettre E apparait environ 17% du temps.
    si dans le texte chiffre, la lettre la plus frequente est H,
    alors le decalage est probablement H - E = 3.
 
    pour etre plus precis, on teste les 26 cles possibles et on
    calcule un score de ressemblance avec les frequences du francais.
    la cle avec le meilleur score est la plus probable.
"""

from .decrypt import decrypt

FREQ_FRANCAIS = {
    'A': 8.11, 'B': 0.81, 'C': 3.38, 'D': 3.69,
    'E': 17.26, 'F': 1.12, 'G': 1.23, 'H': 0.74,
    'I': 7.31, 'J': 0.18, 'K': 0.02, 'L': 5.99,
    'M': 2.62, 'N': 7.23, 'O': 5.29, 'P': 2.78,
    'Q': 1.21, 'R': 6.55, 'S': 8.14, 'T': 7.22,
    'U': 6.05, 'V': 1.32, 'W': 0.04, 'X': 0.45,
    'Y': 0.30, 'Z': 0.12
}

def count_letters(text: str) -> dict:
    """compte le nombre d'occurrences de chaque lettre.
 
    Args:
        text: le texte a analyser
 
    Returns:
        dictionnaire {"A": 5, "B": 0, ...}
    """
 
    counts = {chr(i + ord('A')): 0 for i in range(26)}
 
    for c in text.upper():
        if c.isalpha():
            counts[c] += 1
 
    return counts

 
def compute_frequencies(text: str) -> dict:
    """calcule la frequence de chaque lettre en pourcentage.
 
    Args:
        text: le texte a analyser
 
    Returns:
        dictionnaire {"A": 8.5, "B": 1.2, ...}
    """
 
    counts = count_letters(text)
    total = sum(counts.values())
 
    if total == 0:
        return {letter: 0.0 for letter in counts}
 
    return {letter: (count / total) * 100 for letter, count in counts.items()}

def chi_squared_score(text: str) -> float:
    """calcule le score chi-carre entre les frequences du texte
    et les frequences attendues du francais.
 
    plus le score est bas, plus le texte ressemble a du francais.
 
    formule : sum((observe - attendu)^2 / attendu) pour chaque lettre
 
    Args:
        text: le texte a evaluer
 
    Returns:
        score chi-carre (plus petit = plus probable)
    """
 
    observed = compute_frequencies(text)
    score = 0.0
 
    for letter in FREQ_FRANCAIS:
        expected = FREQ_FRANCAIS[letter]
        if expected > 0:
            score += (observed[letter] - expected) ** 2 / expected
 
    return score
 

def frequency_attack(cipher_text: str) -> list[dict]:
    """attaque par analyse frequentielle.
 
    teste les 26 cles et classe les resultats par score chi-carre.
    le premier resultat est la cle la plus probable.
 
    Args:
        cipher_text: le texte chiffre a attaquer
 
    Returns:
        liste de 26 dictionnaires tries par score croissant :
        [{"key": 3, "text": "HELLO", "score": 12.5}, ...]
    """
 
    results = []
 
    for key in range(26):
        decrypted = decrypt(cipher_text, key)
        score = chi_squared_score(decrypted)
        results.append({"key": key, "text": decrypted, "score": score})
 
    results.sort(key=lambda r: r["score"])
 
    return results
 