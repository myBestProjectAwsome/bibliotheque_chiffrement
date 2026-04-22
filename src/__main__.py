import argparse
from src  import encrypt, decrypt, brute_force


"""CLI pour la bibliotheque de chiffrement de cesar.
 
usage:
    python -m src encrypt "HELLO" 3
    python -m src decrypt "KHOOR" 3
    python -m src crack "KHOOR"
"""

def main():
    parser = argparse.ArgumentParser( description="chiffrement de cesar - chiffrer, dechiffrer et attaquer")

    subparsers = parser.add_subparsers(dest="command", help="commande a executer")
    subparsers.required = True

    # commande encrypt
    encrypt_parser = subparsers.add_parser("encrypt", help="chiffrer un message")
    encrypt_parser.add_argument("text", help="texte a chiffrer")
    encrypt_parser.add_argument("key", type=int, help="cle de decalage (0-25)")
 
    #  commande decrypt 
    decrypt_parser = subparsers.add_parser("decrypt", help="dechiffrer un message")
    decrypt_parser.add_argument("text", help="texte a dechiffrer")
    decrypt_parser.add_argument("key", type=int, help="cle de decalage (0-25)")
 
    #  commande crack 
    crack_parser = subparsers.add_parser("crack", help="attaque par force brute")
    crack_parser.add_argument("text", help="texte chiffre a attaquer")

    args = parser.parse_args()
 
    if args.command == "encrypt":
        result = encrypt(args.text, args.key)
        print(result)
 
    elif args.command == "decrypt":
        result = decrypt(args.text, args.key)
        print(result)
 
    elif args.command == "crack":
        results = brute_force(args.text)
        print(f"texte chiffre : {args.text}")
        print(f"{'cle':<6} {'resultat'}")
        print("-" * 40)
        for r in results:
            print(f"  {r['key']:<4} {r['text']}")

if __name__=="__main__":
    main()
 
