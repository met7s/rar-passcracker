import rarfile
import sys
import os

def crack_rar(rar_path, wordlist_path):
    if not os.path.exists(rar_path):
        print("[!] RAR file not found")
        return

    if not os.path.exists(wordlist_path):
        print("[!] Wordlist not found")
        return

    try:
        rf = rarfile.RarFile(rar_path)
    except:
        print("[!] Failed to open RAR file")
        return

    with open(wordlist_path, "r", errors="ignore") as wordlist:
        for line in wordlist:
            password = line.strip()
            try:
                rf.extractall(pwd=password)
                print(f"\n[✓] PASSWORD FOUND: {password}")
                return
            except:
                print(f"[-] Tried: {password}")

    print("\n[✗] Password not found in wordlist")

if __name__ == "__main__":
    print("=== Simple WinRAR Password Cracker ===")

    rar_file = input("Enter RAR file path: ").strip()
    wordlist = input("Enter wordlist path: ").strip()

    crack_rar(rar_file, wordlist)
