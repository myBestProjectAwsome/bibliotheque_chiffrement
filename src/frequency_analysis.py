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