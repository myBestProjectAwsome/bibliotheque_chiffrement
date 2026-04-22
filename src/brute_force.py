from .decrypt import decrypt
 
def brute_force(cipher_text: str) -> list[dict]:
    """attaque par force brute sur un chiffrement de cesar.
 
    teste les 26 cles possibles et retourne tous les resultats.
 
    Args:
        cipher_text: le texte chiffre a attaquer
 
    Returns:
        liste de 26 dictionnaires {"key": int, "text": str}
    """
 
    results = []
 
    for key in range(26):
        decrypted = decrypt(cipher_text, key)
        results.append({"key": key, "text": decrypted})
 
    return results


def display_brute_force(cipher_text: str) -> None:
    """affiche les 26 resultats de maniere lisible.
 
    Args:
        cipher_text: le texte chiffre a attaquer
    """
 
    results = brute_force(cipher_text)
 
    print(f"=== attaque par force brute ===")
    print(f"texte chiffre : {cipher_text}")
    print(f"{'cle':<6} {'resultat'}")
    print("-" * 40)
 
    for r in results:
        print(f"  {r['key']:<4} {r['text']}")