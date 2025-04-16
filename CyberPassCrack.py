import hashlib
import argparse

def crack_hash(hash_to_crack, wordlist, algo):
    with open(wordlist, 'r') as file:
        for word in file:
            word = word.strip()
            hashed_word = getattr(hashlib, algo)(word.encode()).hexdigest()
            if hashed_word == hash_to_crack:
                print(f"[+] Password found: {word}")
                return word
    print("[-] Password not found")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hash crack tool (ethical )")
    parser.add_argument("-a", "--algo", required=True, help="Hash algoritm (md5, sha256, və s.)")
    parser.add_argument("-i", "--input", required=True, help="Hash value")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")
    args = parser.parse_args()
    crack_hash(args.input, args.wordlist, args.algo)
